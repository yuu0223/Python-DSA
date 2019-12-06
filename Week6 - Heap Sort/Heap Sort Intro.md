# Week6：Heap Sort
## **About Heap Sort**

* Binary Heap(二元堆積)可分為Min Heap與Max Heap兩種。兩者用在排序上，僅僅是順序「由大到小」和「由小到大」的差別。

* 如果要將陣列遞增排序的話就使用Max Heap；如果要遞減排序的話就使用Min Heap。

* Heap Sort步驟:

  (1.) 將資料轉換為 heap 資料結構（遞增排序用 max-heap, 遞減排序選擇 min-heap）。
  
  (2.) 逐步取出最大／最小值，並與最後一個元素置換。具體步驟如下：
       
       (2-1.) 交換 heap 的 root 與最後一個 node，縮小 heap 的範圍（排序一筆資料，故 heap 長度 -1）。
       
       (2-2.) 更新剩下的資料，使其滿足 heap 的特性，稱為 heap ordering property。
       
  (3.) 重複前兩個步驟，直到 heap 中剩最後一個未排序的資料

> Max Heap的條件：

  1 . 父節點的值大於子節點
  
  2 . 樹根(root)一定是所有節點的最大值
  
  ![heapsortmax](https://github.com/yuu0223/code-learning/blob/master/image/heap%20sort%20max.png)

> Min Heap的條件：

  1 . 父節點的值小於子節點
  
  2 . 樹根(root)一定是所有節點的最小值
  
  ![minheapsort](https://github.com/yuu0223/code-learning/blob/master/image/minheapsort.png)
    
  
## **參考資料**
* [堆積排序HeapSort](https://rust-algo.club/sorting/heapsort/)
* [排序(Sorting)](http://spaces.isu.edu.tw/upload/18833/3/web/sorting.htm)
