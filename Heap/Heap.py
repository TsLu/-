#!/usr/bin/env python
# coding=utf-8

class Heap(object):
    def __init__(self):
        data = []
        count = 0
    
    def isEmpty(self):
        """堆是否为空"""
        return self.count == 0
    
    def insert(self, num):
        """
        堆中插入数据num
        """
        #末尾插入，再调整
        self.data.append(num)
        self.count += 1
        self.shiftUp(self.count - 1)
    
    def shiftUp(self, k):
        """
        最大堆核心辅助函数
        """
        while k > 1 and self.data[k / 2] < self.data[k]:
            #交换数据
            self.data[k / 2], self.data[k] = self.data[k], self.data[k / 2]
            
            k = k / 2
    
    def extractMax(self):
        """
        从最大堆中取出堆顶元素, 即堆中所存储的最大数据
        """
        assert self.count > 0
        ret = self.data[1]
        self.data[1] = self.data[self.count - 1]
        self.data.pop()
        self.count -= 1
        self.shiftDown(1)
        return ret
    
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

    def adjustHeap(self, arr, start, end):
        """
        调整最大堆
        """
        #先取出当前元素i
        tmp = arr[start]
        #从start结点的左子结点开始，也就是2start+1处开始
        for k in range(2 * start + 1, end):
            if k + 1 < end and arr[k] < arr[k + 1]:
                #如果左子结点小于右子结点，k指向右子结点
                k += 1
            if arr[k] > tmp:
                #左子节点大于父节点，交换
                arr[start], arr[k] = arr[k], arr[start]
                start = k
            else:
                break
        
        return arr

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
    
        

if __name__ == '__main__':
    obj = Heap()
    #下标从1开始
    obj.data = ['-', 10, 7, 2, 5, 1]
    obj.count = len(obj.data)
    obj.insert(16)
    print obj.data
    obj.extractMax()
    print obj.data
    arr = [1, 20, 16, 18, 9, 15, 21]
    obj.Heapify(arr)
    print obj.data
    
    