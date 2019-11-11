# **Week8：Binary Tree**

## Binary Tree簡介
* 最廣義的樹(Tree)：對於樹上的node之child數目沒有限制，因此，每個node可以有多個child。

     ![tree_pic](https://github.com/yuu0223/code-learning/blob/master/image/tree.png)

* Binary Tree(二元樹)：若限制node只能有兩個child，等價於「樹上的每一個node之degree皆為2」，此即稱為Binary Tree(二元樹)，並稱兩個child pointer為left child和right child。

     ![binarytree_pic](https://github.com/yuu0223/code-learning/blob/master/image/binarytree.png)

> **Full Binary Tree(Perfect Binary Tree)**

    (1.) 所有internal node(內部節點)都有兩個subtree(child pointer)
    
    (2.) 所有leaf node(葉節點)具有相同的level
    
    (3.) 若一棵Full Binary Tree的leaf node之level為n，整棵樹共有(2**n)−1個node。(Ex. level=4(共4層)的樹就有15個node)
    
> **節點的level(階層)、height(高度)、depth(深度)：**
     
     * level(階層)：代表節點間的世代關係
     
     * height(高度)：節點至向下最遠葉節點的距離
     
     * depth(深度)：節點至根節點的距離

     E
