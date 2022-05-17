#!/usr/bin/env python
# coding=utf-8

#邻接表
graph = {'a': ['b', 'c'], 
         'b': ['a', 'c', 'd'], 
         'c': ['a', 'b', 'd'], 
         'd': ['b', 'c', 'e', 'f'], 
         'e': ['d', 'f'], 
         'f': ['d', 'e']}

class DepthSearch(object):
    def __init__(self, graph):
        """初始化"""
        #每个节点所对应的联通分量标记
        self.id = {}
        self.graph = graph

        #记录dfs过程中节点是否已经被访问过, 初始化为都False
        self.visited = {}
        for v in graph:
            self.visited[v] = False
            self.id[v] = -1

        #联通分量个数
        self.ccount = 0
        for v in graph:
            if not self.visited[v]:
                self.dfs(v)
                self.ccount += 1
    
    def dfs(self, v):
        """图的深度优先遍历"""
        self.visited[v] = True
        self.id[v] = self.ccount

        for i in self.graph[v]:
            if not self.visited[i]:
                self.dfs(i)
    
    def getCount(self):
        """返回图的联通分量个数"""
        return self.ccount
    
    def isConnected(self, v, w):
        """查询节点v和节点w是否连通"""
        assert v in self.graph
        assert w in self.graph
        return self.id[v] == self.id[w]
    
if __name__ == '__main__':
    obj = DepthSearch(graph)
    print obj.ccount
    print obj.isConnected('a', 'b')
    
    