## 二分搜索树
以下参考菜鸟教程

### 一、概念及其介绍
二分搜索树（英语：Binary Search Tree），也称为 二叉查找树 、二叉搜索树 、有序二叉树或排序二叉树。满足以下几个条件：
 > 若它的左子树不为空，左子树上所有节点的值都小于它的根节点。
 > 若它的右子树不为空，右子树上所有的节点的值都大于它的根节点。
它的左、右子树也都是二分搜索树。

如下图所示：
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/PbZvFQEItGIFirEP.png" width="70%"/>
</p>

### 二、适用说明
二分搜索树有着高效的插入、删除、查询操作。平均时间的时间复杂度为 O(log n)，最差情况为 O(n)。
二分搜索树与堆不同，不一定是完全二叉树，底层不容易直接用数组表示故采用链表来实现二分搜索树。

|:查找元素|:插入元素|:删除元素|:
|:普通数组|:O(n)|:O(n)|:O(n)|:
|:顺序数组|:O(logn)|:O(n)|:O(n)
|:二分搜索树|:O(logn)|:O(logn)|:O(logn)

### 三、二分查找法过程图示
二分查找法的思想在 1946 年提出，查找问题是计算机中非常重要的基础问题，对于有序数列，才能使用二分查找法。如果我们要查找一元素，先看数组中间的值V和所需查找数据的大小关系，分三种情况：
1、等于所要查找的数据，直接找到
2、若小于 V，在小于 V 部分分组继续查询
2、若大于 V，在大于 V 部分分组继续查询
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/RsvE28BWbRdtJ7YM.png" width="70%"/>
</p>

### 四、二分搜索树深度优先遍历
二分搜索树遍历分为两大类，深度优先遍历和层序遍历。

深度优先遍历分为三种：先序遍历（preorder tree walk）、中序遍历（inorder tree walk）、后序遍历（postorder tree walk），分别为：

1、前序遍历：先访问当前节点，再依次递归访问左右子树。
2、中序遍历：先递归访问左子树，再访问自身，再递归访问右子树。
3、后序遍历：先递归访问左右子树，再访问自身节点。

前序遍历结果图示：
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/traverse-01.png" width="70%"/>
</p>

中序遍历结果图示：
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/traverse-02.png" width="70%"/>
</p>

后序遍历结果图示：
<p align="center">
    <img src="https://www.runoob.com/wp-content/uploads/2020/09/traverse-03.png" width="70%"/>
</p>