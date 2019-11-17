# **Binary Search Tree**
## Binary Search Tree的功能
* Insert - 新增：在最下面root的左子項或右子項新增一個新的value
  
      Insert步驟：
  
      (1.) 判斷是否為空樹，如果是，則將value當成根節點插入。
        
      (2.) 若不是空樹，則判斷是 > root.val或 < root.val
        
      (3.) > root.val則進入右子樹中，< root.val則進入左子樹中
        
      (4.) 重複第三個步驟，直到找到root.left或root.right為None，並新增至root.left或root.right

* Delete - 刪除

* 修改

* Search - 查詢

