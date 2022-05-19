## 并查集基础
以下参考菜鸟教程
### 一、概念及其介绍
并查集是一种树型的数据结构，用于处理一些不相交集合的合并及查询问题。
并查集的思想是用一个数组表示了整片森林（parent），树的根节点唯一标识了一个集合，我们只要找到了某个元素的的树根，就能确定它在哪个集合里。

### 二、应用
并查集用在一些有 N 个元素的集合应用问题中，我们通常是在开始时让每个元素构成一个单元素的集合，然后按一定顺序将属于同一组的元素所在的集合合并，其间要反复查找一个元素在哪个集合中。这个过程看似并不复杂，但数据量极大，若用其他的数据结构来描述的话，往往在空间上过大，计算机无法承受，也无法在短时间内计算出结果，所以只能用并查集来处理。

### 三、并查集的基本数据表示
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/10/union-01.png" width="70%"/>
</p>
如上图 0-4 下面都是 0，5-9 下面都是 1，表示 0、1、2、3、4 这五个元素是相连接的，5、6、7、8、9 这五个元素是相连的。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/10/union-02.png" width="70%"/>
</p>

再如上图 0、2、4、6、8 下面都是 0 这个集合，表示 0、2、4、6、8 这五个元素是相连接的，1、3、5、7、9 下面都是 1 这个集合，表示 0，1、3、5、7、9 这五个元素是相连的。

```python
class UnionFind(obj):
    def __init__(self, n):
        #集合
        self.id = []
        #数据个数
        self.count = n
        #初始化
        for i in range(n):
            self.id[i] = i
```
### 四、基本操作
查询元素所在的集合编号，直接返回 id 数组值，O(1) 的时间复杂度。
```python
class UnionFind(obj):
    def __init__(self, n):
        #集合
        self.id = []
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
    
    def unionElements(p, q):
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
```


### 五、并查集快速合并
对于一组数据，并查集主要支持三个动作：
union(p,q) - 将 p 和 q 两个元素连接起来。
find(p) - 查询 p 元素在哪个集合中。
isConnected(p,q) - 查看 p 和 q 两个元素是否相连接在一起。

上面是用id数组的形式表示并查集，实际操作过程中查找的时间复杂度为 O(1)，但连接效率并不高。

可以用另外一种方式实现并查集。把每一个元素，看做是一个节点并且指向自己的父节点，根节点指向自己。如下图所示，节点 3 指向节点 2，代表 3 和 2 是连接在一起的，节点2本身是根节点，所以指向自己。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/10/quickUnion-01.png" width="70%"/>
</p>

同样用数组表示并查集，但是下面一组元素用 parent 表示当前元素指向的父节点，每个元素指向自己，都是独立的。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/10/quickUnion-02.png" width="70%"/>
</p>

如果此时操作 union(4,3)，将元素 4 指向元素 3：
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/10/quickUnion-04.png" width="70%"/>
</p>

数组也进行相应改变：
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/10/quickUnion-05.png" width="70%"/>
</p>

判断两个元素是否连接，只需要判断根节点是否相同即可。
如下图，节点 4 和节点 9 的根节点都是 8，所以它们是相连的。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/10/quickUnion-06.png" width="70%"/>
</p>
连接两个元素，只需要找到它们对应的根节点，使根节点相连，那它们就是相连的节点。
假设要使上图中的 6 和 4 相连，只需要把 6 的根节点 5 指向 4 的根节点 8 即可。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/10/quickUnion-07.png" width="70%"/>
</p>
构建这种指向父节点的树形结构， 使用一个数组构建一棵指向父节点的树，parent[i] 表示 i 元素所指向的父节点
查找过程, 查找元素 p 所对应的集合编号，不断去查询自己的父亲节点, 直到到达根节点，根节点的特点 parent[p] == p，O(h) 复杂度, h 为树的高度。
合并元素 p 和元素 q 所属的集合，分别查询两个元素的根节点，使其中一个根节点指向另外一个根节点，两个集合就合并了。这个操作是 O(h) 的时间复杂度，h 为树的高度。

```python
class FastUnionFind(object, count):
    def __init__(self):
        #使用一个数组构建一个指向父节点的树
        self.parent = []
        #sz 数组，sz[i] 表示以 i 为根的集合中元素个数
        self.sz = []
        #添加 rank 数组，rank[i] 表示以 i 为根的集合所表示的树的层数
        self.rank = []
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
        if 
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
        if 
        if self.rank[pRoot] < self.range[qRoot]:
            self.parent[pRoot] = qRoot
        elif self.rank[pRoot] > self.range[qRoot]:
            self.parent[qRoot] = pRoot
        else:
            self.parent[pRoot] = qRoot
            #增加层数
            self.rank[pRoot] += 1
```
### 六、并查集路径压缩
并查集里的 find 函数里可以进行路径压缩，是为了更快速的查找一个点的根节点。对于一个集合树来说，它的根节点下面可以依附着许多的节点，因此，我们可以尝试在 find 的过程中，从底向上，如果此时访问的节点不是根节点的话，那么我们可以把这个节点尽量的往上挪一挪，减少数的层数，这个过程就叫做路径压缩。
```python
def findModify(self, p):
        """查找元素p对应的集合编号"""
        assert p >= 0 and p < self.count
        #不断回溯查询父节点，直到到达根节点
        #回溯的过程同时进行路径压缩
        if self.parent[p] != p:
            self.parent[p] = self.findModify(self.parent[p])
        return self.parent[p]
```