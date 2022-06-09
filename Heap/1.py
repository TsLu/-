#!/usr/bin/env python
# coding=utf-8
data_dict = {'datas': [{'a': 'w', 'b': 2, 'c':3}, {'a': '4', 'b': 5, 'c':6}, {'a': 'c', 'b': 2, 'c':6}]}
i=0
for dict_value in data_dict.values():
    print "aa", dict_value, len(dict_value)
    while i < len(dict_value):
    
        print(dict_value), i  #列表
        # print(len(dict_value))
        print(data_dict['datas'][i])
        #以字典的方式获取值
        tup = (data_dict['datas'][i]['a'],data_dict['datas'][i]['b'])
        #或者以列表的方式获取值，dict_value为列表
        tup = (dict_value[i]['a'],dict_value[i]['b'])
        print(tup)
        i = i + 1