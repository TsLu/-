## 堆
以下参考菜鸟教程

### 一、概念及其介绍
堆(Heap)是计算机科学中一类特殊的数据结构的统称。
堆通常是一个可以被看做一棵完全二叉树的数组对象。
堆满足下列性质：
>堆中某个节点的值总是不大于或不小于其父节点的值。
>堆总是一棵完全二叉树。

如下图所示：
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/PbZvFQEItGIFirEP.png" width="70%"/>
</p>

### 二、适用说明
堆是利用完全二叉树的结构来维护一组数据，然后进行相关操作，一般的操作进行一次的时间复杂度在 O(1)~O(logn) 之间，堆通常用于动态分配和释放程序所使用的对象。

若为优先队列的使用场景，普通数组或者顺序数组，最差情况为 O(n^2)，堆这种数据结构也可以提高入队和出队的效率。
入队|出队
-------- | -----
普通数组|O(1)|O(n)
顺序数组|O(n)|O(1)
堆|O(logn)|O(log)


### 三、图示
二叉堆是一颗完全二叉树，且堆中某个节点的值总是不大于其父节点的值，该完全二叉树的深度为 k，除第 k 层外，其它各层 (1～k-1) 的结点数都达到最大个数，第k 层所有的结点都连续集中在最左边。

其中堆的根节点最大称为最大堆，如下图所示：
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/heap-01.png" width="70%"/>
</p>

我们可以使用数组存储二叉堆，右边的标号是数组的索引。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/heap-02.png" width="70%"/>
</p>
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/heap-03.png" width="70%"/>
</p>

假设当前元素的索引位置为 i，可以得到规律：
```python
parent(i) = i/2 #取整
left child(i) = 2*i
right child(i) = 2*i +1
```

### 四、堆添加元素
最大堆中添加元素，称为 shift up。

假设我们对下面的最大堆新加入一个元素52，放在数组的最后一位，52大于父节点16，此时不满足堆的定义，需要进行调整。

<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/shiftUp-01.png" width="70%"/>
</p>

首先交换索引为 5 和 11 数组中数值的位置，也就是 52 和 16 交换位置。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/shiftUp-02.png" width="70%"/>
</p>

此时 52 依然比父节点索引为 2 的数值 41 大，我们还需要进一步挪位置。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/shiftUp-03.png" width="70%"/>
</p>

这时比较 52 和 62 的大小，52 已经比父节点小了，不需要再上升了，满足最大堆的定义。我们称这个过程为最大堆的 shift up。
```python
def shiftUp(self, k):
        """
        最大堆核心辅助函数
        """
        while k > 1 and self.data[k / 2] < self.data[k]:
            #交换数据
            self.data[k / 2], self.data[k] = self.data[k], self.data[k / 2]
            
            k = k / 2
```

###五、堆的shift down
从一个最大堆中取出一个元素，称为 shift down，只能取出最大优先级的元素，也就是根节点。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/shiftDown-01.png" width="70%"/>
</p>


第一步，我们将数组最后一位数组放到根节点，此时不满足最大堆的定义。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/shiftDown-02.png" width="70%"/>
</p>

调整的过程是将这个根节点 16 一步一步向下挪，16 比子节点都小，先比较子节点 52 和 30 哪个大，和大的交换位置。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/zwmoTNoXr132c2OT.png" width="70%"/>
</p>

继续比较 16 的子节点 28 和 41，41 大，所以 16 和 41 交换位置。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/68y5vruWLTnsrcuD.png" width="70%"/>
</p>
继续 16 和孩子节点 15 进行比较，16 大，所以现在不需要进行交换，最后我们的 shift down 操作完成，维持了一个最大堆的性质。

```python
def shiftDown(self, k):
        """
        shiftDown操作
        """
        while 2 * k <= self.count - 1:
            j = 2 * k
            if j + 1 <= self.count - 1 and self.data[j + 1] > self.data[j]:
                j += 1
            
            if self.data[k] > self.data[j]:
                break
            else:
                self.data[k], self.data[j] = self.data[j], self.data[k]
                k = j
```
### 六、基础堆排序
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。

堆是一个近似 完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点

完全二叉树有个重要性质，对于第一个非叶子节点的索引是 n/2 取整数得到的索引值，其中 n 是元素个数(前提是数组索引从 1 开始计算)。

<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/heapify-01.png" width="70%"/>
</p>

索引 5 位置是第一个非叶子节点，我们从它开始逐一向前分别把每个元素作为根节点进行 shift down 操作满足最大堆的性质。
索引 5 位置进行 shift down 操作后，22 和 62 交换位置。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/heapify-02.png" width="70%"/>
</p>
对索引 4 元素进行 shift down 操作
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/heapify-03.png" width="70%"/>
</p>
对索引 3 元素进行 shift down 操作
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/heapify-04.png" width="70%"/>
</p>
对索引 2 元素进行 shift down 操作
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/heapify-05.png" width="70%"/>
</p>
最后对根节点进行 shift down 操作，整个堆排序过程就完成了。
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/heapify-06.png" width="70%"/>
</p>
```python
    def Heapify(self, arr):
        """
        通过一个给定数组创建一个最大堆
        该构造堆的过程, 时间复杂度为O(n)
        """
        l = len(arr)
        self.data = []
        for i in arr:
            self.data.append(i)
        self.count = len(self.data)

        #从第一个不是叶子节点的元素开始
        i = l / 2
        
        #1.构建大顶堆
        while i >= 0:
            self.data = self.adjustHeap(self.data, i, self.count)
            i -= 1
        
        #2.调整堆结构 + 交换堆顶元素与末尾元素
        j = self.count - 1
        while j > 0:
            self.data[0], self.data[j] = self.data[j], self.data[0]
            self.data = self.adjustHeap(self.data, 0, j)
            j -= 1
```