#!/usr/bin/env python
# coding=utf-8

class DenseGraph(object):
    def __init__(self, vertex, edge, directed):
        #节点数
        self.vertex = vertex
        #边数
        self.edge = edge
        #是否有向图
        self.directed = directed
        #图的具体数据, 初始化为Fasle, 无任何边
        self.graph = [[False] * vertex for _ in range(vertex)]
    
    def getVertexNum(self):
        """获取节点个数"""
        return self.vertex
    
    def getEdgeNum(self):
        """获取边的个数"""
        return self.edge
    
    def addEdge(self, v, w):
        """向图中添加一个便"""
        assert v >= 0 and v < self.vertex
        assert w >= 0 and w < self.vertex
        #如果已经存在边了，直接返回
        if self.hasEdge(v, w):
            return
        self.graph[v][w] = True
        #非有向图, 双向的
        if not self.directed:
            self.graph[w][v] = True
        #边数加1
        self.edge += 1
    
    def hasEdge(self, v, w):
        """判断图中是否有从v到w的边"""
        assert v >= 0 and v < self.vertex
        assert w >= 0 and w < self.vertex
        return self.graph[v][w]
    
    def getAllEdge(self, v):
        """获取图中一个点的所有邻边"""
        assert v >= 0 and v < self.vertex
        res = []
        for i in range(self.vertex):
            if self.graph[v][i]:
                res.append(i)
        
        return res

if __name__ == '__main__':
    obj = DenseGraph(3, 2, False)
    print obj.graph
    print obj.hasEdge(1, 2)
    obj.addEdge(1, 2)
    print obj.graph
    print obj.hasEdge(1, 2)