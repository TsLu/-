#!/usr/bin/env python
# coding=utf-8

#邻接表
graph = {'a': ['b', 'c'], 
         'b': ['a', 'c', 'd'], 
         'c': ['a', 'b', 'd'], 
         'd': ['b', 'c', 'e', 'f'], 
         'e': ['d', 'f'], 
         'f': ['d', 'e']}
         
class Path(object):
    def __init__(self, graph, s):
        self.graph = graph
        #起始点
        self.s = s
        #记录路径，from_arr[i]表示查找的路径上i的上一个节点
        self.from_arr = {}
        #记录dfs过程中节点是否已经被访问过, 初始化为都False
        self.visited = {}
        for v in graph:
            self.visited[v] = False
            self.from_arr[v] = '-1'
        #寻路算法
        self.dfs(s)

    def dfs(self, s):
        """图的深度优先遍历"""
        self.visited[s] = True
        for v in self.graph[s]:
            if not self.visited[v]:
                self.from_arr[v] = s
                self.dfs(v)
        
    def hasPath(self, w):
        """查询从s点到w点是否有路径"""
        assert w in self.graph
        return self.visited[w]
        
    def getPath(self, w):
        """查询从s点到w点的路径，存放在vec中"""
        assert self.hasPath(w)
        tmp_s = []
        p = w
        while p != '-1':
            tmp_s.append(p)
            p = self.from_arr[p]
        #从栈中依次取出元素，获得从s到w的路径
        res = []
        while tmp_s:
            res.append(tmp_s.pop())
            
        return res
        
    def showPath(self, w):
        """打印从s到w带你的路径"""
        assert self.hasPath(w)
        path = self.getPath(w)
        msg = ''
        for i in range(len(path)):
            msg = msg + path[i]
            if i == len(path) - 1:
                msg = msg + "\n"
            else:
                msg = msg + " -> "
        print msg
        
if __name__ == '__main__':
    obj = Path(graph, 'a')
    print obj.hasPath('b')
    obj.showPath('f')