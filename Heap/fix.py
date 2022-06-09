#!/usr/bin/env python
# coding=utf-8
"""
 @auth : lutingshu@baidu.com
 @date : 2022-06-08 11:41:21
"""

import argparse
import pymysql
import logging
import requests
import json

db_config = {
    'host': '10.144.222.35',
    'port': 8306,
    'user': 'root',
    'password': 'MhxzKhl@35',
    'database': 'auto_test',
    'charset': 'UTF8'
}

class AgileDb(object):
    """agile db 操作"""
    def __init__(self):
        """初始化"""
        try:
            config = db_config
            self.conn = pymysql.connect(**config)
            self.cur = self.conn.cursor()
        except:
            logging.error('init error!')

    def DbClose(self):
        """close"""
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()

    def NoQaFix(self):
        """判断q是否有qa触发任务"""
        sql = "select build_id, build_number, branch, module from agile_test_result where create_time >= '2022-04-01'"
        #sql = "select build_id, build_number, branch, module from agile_test_result where id = 769"
        self.cur.execute(sql)
        db_result = self.cur.fetchall()
        for item in db_result:
            build_id = item[0]
            build_number = item[1]
            branch = item[2]
            module = item[3]
            '''
            sql = "select user from agile_test_time where module = '%s'" % (module) + \
                "and branch = '%s' and build_number='%s' group by user;"\
                % (branch, build_number)
            print sql
            self.cur.execute(sql)
            db_result = self.cur.fetchall()
            '''
            if build_number == '':
                continue
            """获取当前分支的触发人，从数据中台拿"""
            request_header = dict()
            request_header['name'] = 'zhaoyiming01'
            request_header['token'] = 'd2d3232a5848438fbc50c7cbdf007845'
            request_header['Content-Type'] = 'application/json'
            request_data =dict()
            request_data[
                'sql'] = "SELECT AGILE_TRIGGER_USER FROM CICD_BASIC_INFO WHERE AGILE_COMPILE_BRANCH='%s' \
                    AND AGILE_MODULE_NAME='%s' AND AGILE_PIPELINE_BUILD_NUMBER = %s \
                    AND AGILE_PIPELINE_NAME !='ChangePipeline' group by AGILE_TRIGGER_USER " \
                 % (branch, module, build_number)
            url = 'http://qadc.baidu-int.com/api/query'
            response = requests.post(url,
                            headers=request_header,
                            data=json.dumps(request_data)).json()
            
            qa_set = set()
            n = len(response['data']['details'])
            
            for i in range(n):
                u = response['data']['details'][i]['AGILE_TRIGGER_USER']
                qa_set.add(u)
            print qa_set
            sql = "select user_name from qa_list ;"
            self.cur.execute(sql)
            db_result = self.cur.fetchall()
            all_qa_set = set()
            for item in db_result:
                all_qa_set.add(item[0])
            #print all_qa_set
            no_qa = "YES" if len(qa_set & all_qa_set) == 0 else "NO"
            sql = "update agile_test_result set no_qa='{}' where build_id='{}' and module = '{}';"\
                .format(no_qa, build_id, module)
            print(sql)
            self.cur.execute(sql)
            self.conn.commit()
        self.DbClose()

if __name__ == "__main__":
    db = AgileDb()
    db.NoQaFix()
