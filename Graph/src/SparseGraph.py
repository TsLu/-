#!/usr/bin/env python
# coding=utf-8

class SparseGraph(object):
    def __init__(self, vertex, edge, directed):
        #节点数
        self.vertex = vertex
        #边数
        self.edge = edge
        #是否有向图
        self.directed = directed
        #图的具体数据, 初始化为空的vector，表示每一个g[i]都为空，也就是没有任何的边
        self.graph = [[] * vertex for _ in range(vertex)]
    
    def getVertexNum(self):
        """获取节点个数"""
        return self.vertex
    
    def getEdgeNum(self):
        """获取边的个数"""
        return self.edge
    
    def addEdge(self, v, w):
        """向图中添加边"""
        assert v >= 0 and v < self.vertex
        assert w >= 0 and w < self.vertex
        self.graph[v].append(w)
        #非有向图
        if v != w and not self.directed:
            self.graph[w].append(v)
        self.edge += 1
    
    def hasEdge(self, v, w):
        """验证图中是否有从v到w的边"""
        assert v >= 0 and v < self.vertex
        assert w >= 0 and w < self.vertex
        if w in self.graph[v]:
            return True
        return False
    
    def getAllEdge(self, v):
        """获取图中一个点的所有邻边"""
        assert v >= 0 and v < self.vertex
        return self.graph[v]

if __name__ == '__main__':
    obj = SparseGraph(3, 2, False)
    print obj.graph
    print obj.hasEdge(1, 2)
    obj.addEdge(1, 2)
    print obj.graph
    print obj.hasEdge(1, 2)
    