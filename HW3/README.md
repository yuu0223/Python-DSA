# **Binary Search Tree**
## Binary Search Tree的功能
* **Insert - 新增**：在Binary tree最下面root的左子項或右子項新增一個新的value。
  
      Insert步驟：
  
      (1.) 判斷是否為空樹，如果是，則將value當成根節點插入
        
      (2.) 若不是空樹，則判斷是 > root.val或 < root.val
        
      (3.) > root.val則進入右子樹中，< root.val則進入左子樹中
        
      (4.) 重複第三個步驟，直到找到root.left或root.right為None，並新增至root.left或root.right

![bst_insert](https://github.com/yuu0223/code-learning/blob/master/image/bst_insert.jpg)

* **Delete - 刪除**：在Binary tree中找到符合我們要刪除的value並刪除。

      Delete步驟：
      
      (1.) 判斷是否為空樹，如果是，則不做任何動作
      
      (2.) 若不是空樹，則先判斷是否有左子樹或右子樹
      
      (3.) 若有左子樹and沒有右子樹，則將root.left.val直接取代root.val
      
      (4.) 若有右子樹，則將key下面的所有root.right往上移，取代他們的parent

![bst_del](https://github.com/yuu0223/code-learning/blob/master/image/bst_delete.jpg)

* **修改**

* **Search - 查詢**：

![bst_search](https://github.com/yuu0223/code-learning/blob/master/image/bst_search.jpg)


## Reference

* [維基百科 - 二元搜尋樹](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9)

* [資料結構 - 二元搜索樹](https://emn178.pixnet.net/blog/post/94574434)

* [Binary search tree(Intro) By Chiu CC ](http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html#insert)
