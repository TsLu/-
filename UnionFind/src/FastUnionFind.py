#!/usr/bin/env python
# coding=utf-8

class FastUnionFind(object):
    def __init__(self, count):
        #使用一个数组构建一个指向父节点的树
        self.parent = [None] * count
        #sz 数组，sz[i] 表示以 i 为根的集合中元素个数
        self.sz = [None] * count
        #添加 rank 数组，rank[i] 表示以 i 为根的集合所表示的树的层数
        self.rank = [None] * count
        #数据个数
        self.count = count
        #初始化，每一个parent[i]指向自己，表示每个元素自己自成一个集合
        for i in range(count):
            self.parent[i] = i
            self.sz[i] = 1
            self.rank[i] = 1
    
    def find(self, p):
        """查找元素p所对应的集合编号"""
        assert p >= 0 and p < self.count
        #不断回溯查询父节点，直到到达根节点
        while p != self.parent[p]:
            p = self.parent[p]
        return p
    
    def findModify(self, p):
        """查找元素p对应的集合编号"""
        assert p >= 0 and p < self.count
        #不断回溯查询父节点，直到到达根节点
        #回溯的过程同时进行路径压缩
        if self.parent[p] != p:
            self.parent[p] = self.findModify(self.parent[p])
        return self.parent[p]
    
    def isConnected(self, p, q):
        """查找元素p和元素q是否在同一个集合中"""
        return self.find(p) == self.find(q)
    
    def unionElements(self, p, q):
        """合并元素p和元素q所属的集合"""
        pRoot = self.find(p)
        qRoot = self.find(q)
        #本身已经在同一个集合中
        if pRoot == qRoot:
            return
        self.parent[pRoot] = qRoot
    
    def unionElementsBySize(self, p, q):
        """
        合并元素p和元素q所属的集合
        在进行具体指向操作的时候先进行判断，把元素少的集合根节点指向元素多的根节点，能更高概率的生成一个层数比较低的树。
        """
        pRoot = self.find(p)
        qRoot = self.find(q)
        #本身已经在同一个集合中
        if pRoot == qRoot:
            return
        
        if self.sz(pRoot) < self.sz[qRoot]:
            self.parent[pRoot] = qRoot
            self.sz[qRoot] += self.sz[pRoot]
        else:
            self.parent[qRoot] = pRoot
            self.sz[pRoot] += self.sz[qRoot]
    

    def unionElementsByRank(self, p, q):
        """
        合并元素p和元素q所属的集合
        依靠集合的 size 判断指向并不是完全正确的，
        更准确的是，根据两个集合层数，具体判断根节点的指向，
        层数少的集合根节点指向层数多的集合根节点
        """
        pRoot = self.find(p)
        qRoot = self.find(q)
        #本身已经在同一个集合中
        if pRoot == qRoot:
            return
        
        if self.rank[pRoot] < self.range[qRoot]:
            self.parent[pRoot] = qRoot
        elif self.rank[pRoot] > self.range[qRoot]:
            self.parent[qRoot] = pRoot
        else:
            self.parent[pRoot] = qRoot
            #增加层数
            self.rank[pRoot] += 1
    

if __name__ == '__main__':
    obj = FastUnionFind(8)
    print obj.find(1)
    print obj.isConnected(1, 2)
    obj.unionElements(1, 2)
    print obj.isConnected(1, 2)
    print obj.isConnected(2, 6)
    print obj.find(1)
    obj.unionElements(2, 6)
    print obj.findModify(2)
    print obj.findModify(1)




