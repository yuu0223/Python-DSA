# **Heap Sort & Merge Sort之比較**

> **Heap Sort簡介** 
* Binary Heap(二元堆積)可分為Min Heap與Max Heap兩種。兩者用在排序上，僅僅是順序「由大到小」和「由小到大」的差別。

* Heap Sort步驟:

  (1.) 將資料轉換為 heap 資料結構（遞增排序用 max-heap, 遞減排序選擇 min-heap）。
  
  (2.) 逐步取出最大／最小值，並與最後一個元素置換。具體步驟如下：
       
       (2-1.) 交換 heap 的 root 與最後一個 node，縮小 heap 的範圍（排序一筆資料，故 heap 長度 -1）。
       
       (2-2.) 更新剩下的資料，使其滿足 heap 的特性，稱為 heap ordering property。
       
  (3.) 重複前兩個步驟，直到 heap 中剩最後一個未排序的資料

> **Merge Sort簡介**
* Merge Sort(又稱為「合併排序法」)屬於Divide and Conquer演算法，把問題先拆解(divide)成子問題，並在逐一處理子問題後，將子問題的結果合併(conquer)，如此便解決了原先的問題。

* Merge Sort步驟:

  (1.) 當數列僅剩一個元素(len(數列)<=1)時即回傳
 
  (2.) 當數列不僅一個元素(len(數列)>1)時，切割後待子數列排序完成
 
  (3.) 取得兩個有序子數列後，利用兩個指標指向該兩個子數列的起始元素
 
  (4.) 比較兩指標所指到的值，並將較小者放入原數列，並將指標指向下一個元素
 
  (5.) 若某一個指標已指到數列結尾，則按照順序將另一個子數列剩餘的元素放到原數列中
 
  (6.) 反覆進行以上步驟即可排序完成

## **Heap Sort v.s Merge Sort**

## **參考資料**
* [Comparison Sort:Merge Sort By Chiu CC](http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html)
* [Sort 淺談 merge sort](https://blog.kuoe0.tw/posts/2013/03/06/sort-about-merge-sort/)
