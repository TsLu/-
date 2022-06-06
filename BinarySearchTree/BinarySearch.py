#!/usr/bin/env python
# coding=utf-8
def BinarySearch(nums, target):
    """二分查找算法"""
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l)/ 2
        #找到了
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    return - 1

class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self):
        #数的根节点
        self.root = None
        #数的个数
        self.count = 0
    
    def isEmpty(self):
        """二叉搜索树是否为空"""
        return self.count == 0
    
    def insert(self, value):
        """二分搜索树中插入新的节点"""
        #首先要添加新的节点，首先需要创建 Node 对象，将数据传入该对象
        newNode = Node(value, None, None)
        #是否有根节点，没有的话，说明是一个新树，插入节点就是该树的根节点
        if self.root == None:
            self.root = newNode
            self.count += 1
        else:
            #待插入的节点不是根节点，需要遍历，将其放入合适的位置
            #设置当前节点为根节点
            curNode = self.root
            while True:
                parentNode = curNode
                if value < curNode.value:
                    #插入的value小于当前节点，则新的节点为当前节点的左子树
                    curNode = curNode.left
                    #如果当前节点的左子树为空，直接将新节点放在左子树上
                    if curNode == None:
                        parentNode.left = newNode
                        self.count += 1
                        break
                else:
                    #插入的value大于当前节点，则新的节点为当前节点的右子树
                    curNode = curNode.right
                    #如果当前节点的右子树为空，直接将新节点放在右子树上
                    if curNode == None:
                        parentNode.right = newNode
                        self.count += 1
                        break
    
    def insert2(self, node, value):
        #是否有根节点，没有的话，说明是一个新树，插入节点就是该树的根节点
        if node == None:
            newNode = Node(value, None, None)
            self.count += 1
            return newNode
        #搜索插入位置，使用递归算法，返回插入的新节点后的二分搜索树的根节点
        if value < node.value:
            #如果当前节点的左子树为空，直接将新节点放在左子树上
            if node.left == None:
                node.left = Node(value, None, None)
                self.count += 1
                return node
            else:
                node.left = self.insert2(node.left, value)
        elif value > node.value:
            #如果当前节点的右子树为空，直接将新节点放在右子树上
            if node.right == None:
                node.right = Node(value, None, None)
                self.count += 1
                return node
            else:
                node.right = self.insert2(node.right, value)
        else:
            node.value = value
        return node
    
    def contain(self, node, value):
        """查看以node为根的二分搜索树中是否包含键值为key的节点, 使用递归算法"""
        if node == None:
            return False
        if node.value == value:
            return True
        elif node.value < value:
            if node.right == None:
                return False
            return self.contain(node.left, value)
        else:
            if node.right == None:
                return False
            return self.contain(node.right, value)
        
        return False
    
    def preOrder(self, node):
        """前序遍历,递归"""
        if node == None:
            return
        print node.value
        self.preOrder(node.left)
        self.preOrder(node.right)
    
    def inOrder(self, node):
        """中序遍历，递归"""
        if node == None:
            return
        self.inOrder(node.left)
        print node.value
        self.inOrder(node.right)
    
    def postOrder(self, node):
        """后序遍历，递归"""
        if node == None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print node.value

    def levelOrder(self, node):
        """层级遍历"""
        import Queue
        q = Queue.Queue
        q.put(node)
        while ! q.isEmpty():
            curNode = q.pop()
            print curNode.value
            if curNode.left:
                q.put(curNode.left)
            if curNode.right:
                q.put(curNode.right)
    
    def min_node(node):
        """
        返回以node为根的二分搜索树的最小键值所在的节点
        """
        if node.left is None:
            return node
        else:
            return min_node(node.left)
    
    def removeMin(node):
        """
        删除掉以node为根的二分搜索树中的最小节点
        返回删除节点后新的二分搜索树的根
        """
        if node.left is None:
            right_node = node.right
            node.right = None
            self.count -= 1
            return right_node
        node.left = self.reMoveMin(node.left)
        return node
    
    def delete(self, value):
        """
        删除掉以node为根的二分搜索树中键值为value的节点, 递归算法
        返回删除节点后新的二分搜索树的根
        """
        if node == None:
            return
        if node.value > value:
            node.right = self.delete(node.right, value)
            return node
        elif node.value < value:
            node.left = self.delete(node.left, value)
            return node
        else:
            #value等于当前的节点的值
            #如果当前节点的左子树为空
            if node.left is None:
                right_node = node.right
                node.right = None
                self.count -= 1
                return right_node 
            elif node.right is None:
                #如果当前节点的右子树为空
                left_node = node.left
                node.left = None
                self.count -= 1
                return left_node
            else:
                #待删除的左右子树都不为空的情况
                #找到右子树中比待删除节点大的最小节点, 即待删除节点右子树的最小节点
                #用这个节点顶替待删除节点的位置
                find_min = self.min_node(node.right)
                self.count += 1
                
                find_min.right = self.reMoveMin(node.right)
                find_min.left = node.left
                node.left = node.right = None
                self.count -= 1
                return find_min


                

        



    


        
        
    
