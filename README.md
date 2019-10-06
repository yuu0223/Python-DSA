# 108-1 Data Structure and Algorithm(DSA)
# Week1
****

# Week2 : Linked-List
## **About Linked-List**

* Linked list 是一種常見的資料結構，使用node(節點)來記錄、表示及儲存資料，並利用每個node中的pointer(指標)指向下一個node，藉此將多個node串連起來，形成Linked list，並以NULL來代表Linked list的終點。

## **Linked-List v.s. Array**
> **Linked-List**
* 優點：

   * 新增/刪除資料較簡單，只需要調整O(1)個node的pointer，不需要像Array動到其他元素。
   
   * Linked List的資料數量可以是動態的，不像Array會有resize(重新配置大小)的問題。
   
* 缺點：

  * 由於Linked List沒有index，要搜索特定的node時，只能從頭開始搜索，而搜尋的時間複雜度為O(N)。
  
  * 需要額外的空間來儲存pointer。
  
> **Array**

* 優點：

  * 較Linked list為節省記憶體空間->因為Linked List還需要空間儲存pointer。
  
  * random access(隨機存取)->只要利用index即可在O(1)時間對Array的資料做存取。

* 缺點：

  * 新增/刪除資料較麻煩->若要新增/刪除第一個資料，則需要花O(N)時間把矩陣中所有元素往後/前移動。
  
  * 若資料量時常在改變，要時常調整矩陣大小(resize)，會花費O(N)時間在搬移資料(從舊矩陣移到新矩陣)。

## **參考資料**
* [維基百科 - Linked-list(連結串列)](https://zh.wikipedia.org/wiki/%E9%93%BE%E8%A1%A8)
* [Linked List 簡介 By Chiu CC](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)

# Week3 : Stack、Queue


# Week4 : Insertion Sort、Quick Sort
