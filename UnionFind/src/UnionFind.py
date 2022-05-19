#!/usr/bin/env python
# coding=utf-8

class UnionFind(object):
    def __init__(self, n):
        #集合
        self.id = [None] * n
        #数据个数
        self.count = n
        #初始化
        for i in range(n):
            self.id[i] = i
        
    def find(self, p):
        """查找元素p所对应的集合编号"""
        assert p >= 0 and p < self.count
        return self.id[p]
    
    def isConnected(self, p, q):
        """查看元素p和元素q是否在同一个集合中"""
        return self.find(p) == self.find(q)
    
    def unionElements(self, p, q):
        """合并元素p和元素q的集合"""
        pId = self.find(p)
        qId = self.find(q)
        #本身就在同一个集合
        if pId == qId:
            return
        #合并过程需要遍历一遍元素，将两个元素的所属集合编号合并
        for i in range(self.count):
            if self.id[i] == pId:
                self.id[i] = qId
        
    
if __name__ == '__main__':
    obj = UnionFind(8)
    print obj.find(1)
    print obj.isConnected(1, 2)
    obj.unionElements(1, 2)
    print obj.isConnected(1, 2)

    

        
