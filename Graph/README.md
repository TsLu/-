#图论基础和表示
以下参考菜鸟教程
##一、基础概念
图论(Graph Theory)是离散数学的一个分支，是一门研究图(Graph)的学问。

图是用来对对象之间的成对关系建模的数学结构，由"节点"或"顶点"(Vertex）以及连接这些顶点的"边"（Edge）组成。

图的顶点集合不能为空，但边的集合可以为空。图可能是无向的，这意味着图中的边在连接顶点时无需区分方向。否则，称图是有向的。

<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/10/graph-01.png" width="70%"/>
</p>

图的分类：无权图和有权图，连接节点与节点的边是否有数值与之对应，有的话就是有权图，否则就是无权图。

图的连通性：在图论中，连通图基于连通的概念。在一个无向图 G 中，若从顶点 i 到顶点 j 有路径相连（当然从j到i也一定有路径），则称 i 和 j 是连通的。如果 G 是有向图，那么连接i和j的路径中所有的边都必须同向。如果图中任意两点都是连通的，那么图被称作连通图。如果此图是有向图，则称为强连通图（注意：需要双向都有路径）。图的连通性是图的基本性质。

完全图：完全是一个简单的无向图，其中每对不同的顶点之间都恰连有一条边相连。

自环边：一条边的起点终点是一个点。

平行边：两个顶点之间存在多条边相连接。

##二、基本应用
图可用于在物理、生物、社会和信息系统中建模许多类型的关系和过程，许多实际问题可以用图来表示。因此，图论成为运筹学、控制论、信息论、网络理论、博弈论、物理学、化学、生物学、社会科学、语言学、计算机科学等众多学科强有力的数学工具。在强调其应用于现实世界的系统时，网络有时被定义为一个图，其中属性(例如名称)之间的关系以节点和或边的形式关联起来。

###三、图的表达形式
邻接矩阵：1 表示相连接，0 表示不相连。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/10/graph-02.png" width="70%"/>
</p>

邻接表：只表达和顶点相连接的顶点信息
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/10/graph-03.png" width="70%"/>
</p>

邻接表适合表示稀疏图 (Sparse Graph)

邻接矩阵适合表示稠密图 (Dense Graph)

###四、邻接矩阵和邻接表的代码示例
1、邻接矩阵
```python
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
```

2、邻接表
```python
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
```

###五、深度优先遍历与连通分量
深度优先遍历(Depth First Search)的主要思想是首先以一个未被访问过的顶点作为起始顶点，沿当前顶点的边走到未访问过的顶点。当没有未访问过的顶点时，则回到上一个顶点，继续试探别的顶点，直至所有的顶点都被访问过。

下图示例的图从 0 开始遍历顺序如右图所示：
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/10/deep-01.png" width="70%"/>
</p>

无向图 G 的一个极大连通子图称为 G 的一个连通分量（或连通分支）。连通图只有一个连通分量，即其自身；非连通的无向图有多个连通分量。连通分量与连通分量之间没有任何边相连。深度优先遍历可以用来求连通分量。

下面以求连通分量为例，来实现图的深度优先遍历，称为 dfs。下面代码片段中，visited 数组记录 dfs 的过程中节点是否被访问，ccount 记录联通分量个数，id 数组代表每个节点所对应的联通分量标记，两个节点拥有相同的 id 值代表属于同一联通分量。
```python
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
```
###六、寻路算法
图的寻路算法也可以通过深度优先遍历 dfs 实现，寻找图 graph 从起始 s 点到其他点的路径，在上一小节的实现类中添加全局变量 from数组记录路径，from[i] 表示查找的路径上i的上一个节点。

首先构造函数初始化寻路算法的初始条件，from = new int[G.V()] 和 from = new int[G.V()]，并在循环中设置默认值，visited 数组全部为false，from 数组全部为 -1 值，后面对起始节点进行 dfs 的递归处理。
```python
class Path(object):
    def __init__(self, graph, s):
        self.graph = graph
        #起始点
        self.s = s
        #记录路径，from[i]表示查找的路径上i的上一个节点
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
```

###七、广度优先遍历与最短路径
广度优先遍历从某个顶点 v 出发，首先访问这个结点，并将其标记为已访问过，然后顺序访问结点v的所有未被访问的邻接点 {vi,..,vj} ，并将其标记为已访问过，然后将 {vi,...,vj} 中的每一个节点重复节点v的访问方法，直到所有结点都被访问完为止。

我们可以分为三个步骤：
（1）使用一个辅助队列 q，首先将顶点 v 入队，将其标记为已访问，然后循环检测队列是否为空。
（2）如果队列不为空，则取出队列第一个元素，并将与该元素相关联的所有未被访问的节点入队，将这些节点标记为已访问。
（3）如果队列为空，则说明已经按照广度优先遍历了所有的节点。

下图所示，右边蓝色表示从 0 开始遍历节点的顺序，下面是记录距离 0 的距离，可知广度优先遍历能求出无权图的最短路径。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/10/shortest-01.png" width="70%"/>
</p>

使用全局变量 ord 数组，记录路径中节点的次序。ord[i] 表示 i 节点在路径中的次序。同时构造函数做出相应调整，在遍历相邻节点时 每访问一个未被访问的节点进行 ord[i] = ord[v] + 1记录距离。邻接表的广度优先遍历时间复杂度为 O(V+E)，邻接矩阵的时间复杂度为O(V^2)。

```python
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
```