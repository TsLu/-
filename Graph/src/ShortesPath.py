#!/usr/bin/env python
# coding=utf-8

#邻接表
graph = {'a': ['b', 'c'], 
         'b': ['a', 'c', 'd'], 
         'c': ['a', 'b', 'd'], 
         'd': ['b', 'c', 'e', 'f'], 
         'e': ['d', 'f'], 
         'f': ['d', 'e']}

class ShortestPath(object):
    def __init__(self, graph, s):
        self.graph = graph
        #起始点
        self.s = s
        #记录路径，from_arr[i]表示查找的路径上i的上一个节点
        self.from_arr = {}
        #记录dfs过程中节点是否已经被访问过, 初始化为都False
        self.visited = {}
        #记录路径中节点的次序，ord[i]表示i节点在路径中的次序
        self.ord = {}
        #初始化
        for v in graph:
            self.visited[v] = False
            self.from_arr[v] = '-1'
            self.ord[v] = '-1'
        
        #无向图最短路径算法，从s开始广度优先遍历整张图
        import Queue
        q = Queue.Queue()
        q.put(s)
        self.visited[s] = True
        self.ord[s] = 0
        while not q.empty():
            v = q.get()
            for i in graph[v]:
                if not self.visited[i]:
                    q.put(i)
                    self.visited[i] = True
                    self.from_arr[i] = v
                    self.ord[i] = self.ord[v] + 1
        
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

    def length(self, w):
        """查看从s点到w点的最短路径长度"""
        assert w in self.graph
        return self.ord[w]

if __name__ == '__main__':
    obj = ShortestPath(graph, 'a')
    print obj.hasPath('b')
    obj.showPath('f')
    print obj.length('f')

        

