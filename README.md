# 108-1 Data Structure and Algorithm(DSA)
# About Me
* Name：陳品伃
* Birth：1999.05.27
* Constellation：Gemini
* Major：SCU Big Data Management
* contact：pennychen1999@icloud.com

# Content
* [**Week2：Linked-List**](https://github.com/yuu0223/code-learning/tree/master/Week2%20-%20Linked%20List)
  * Leetcode - 707. Design Linked List
* [**Week3：Stack & Queue**](https://github.com/yuu0223/code-learning/tree/master/Week3%20-%20Stack%20%26%20Queue)
  * [Leetcode - 155. Min Stack](https://github.com/yuu0223/code-learning/blob/master/Week3%20-%20Stack%20%26%20Queue/155.%20MinStack.py)
  * [Leetcode - 232. Implement Queue](https://github.com/yuu0223/code-learning/blob/master/Week3%20-%20Stack%20%26%20Queue/232.%09%20Implement%20Queue.py)
* [**Week4：Insertion sort & Quick sort**](#week4--insertion-sort--quick-sort)
  * [HW1 - Quick Sort](https://github.com/yuu0223/code-learning/tree/master/HW1%20-%20Quick%20Sort)
  * Leetcode - 147. Insertion Sort List
  * [Leetcode - 645. Set Mismatch](https://github.com/yuu0223/code-learning/blob/master/Week4/645.%20Set%20Mismatch.py)
* [**Week6：Heap Sort**](#Week6Heap-Sort)
* [**Week7：Merge Sort**](#Week7Merge-Sort)
  * [HW2 - Heap Sort & Merge Sort](https://github.com/yuu0223/code-learning/tree/master/HW2%20-%20Heap%20Sort%20%26%20Merge%20Sort)

# Week3 : Stack & Queue
## **About Stack**
* Stack是具有LIFO(Last-In-First-Out)的資料結構，如同把書堆疊起來，最下面的書最先進入書堆中也最晚被取走，最上面的書最晚進入書堆中卻最早被取走。

* 一般的Stack，會有以下幾項處理資料結構的功能：

  * Push()：將資料加入Stack的最後方(top)。
  
  * Pop()：將最後進入(top)Stack的資料取出。
  
  * Top()：回傳Stack最頂端(top)的資料。
  
  * IsEmpty()：回傳Stack中是否有資料。
  
  * getSize()：回傳Stack的資料個數。
  
* Stack的應用：

  * 編輯器(如word)的undo(返回上一步)。
  
  * 瀏覽器的返回上一頁。
  
## **About Queue**
* Queue是具有FIFO(First-In-First-Out)的資料結構，如同排隊買票的隊伍，先進入隊伍的人，就可以優先買到票，而後到的人，則需要等隊伍前面的人都買完票後才能買。

* 一般的Queue，會有以下幾項處理資料結構的功能：

  * Push()：將資料加入Queue的最後方，成為新的back。(在Queue中新增資料稱為enqueue)
  
  * Pop()：將Queue最前方(最先加入)的資料刪除，並更新front。(在Queue中刪除資料稱為dequeue)
  
  * getFront()：回傳Queue的首項。
  
  * getBack()：回傳Queue的末項。
  
  * IsEmpty()：回傳Queue中是否有資料。
  
  * getSize()：回傳Queue的資料個數。
  
## **Reference**
* [Queue簡介 By Chiu CC](http://alrightchiu.github.io/SecondRound/queue-introjian-jie-bing-yi-linked-listshi-zuo.html#intro)
* [Stack簡介 By Chiu CC](http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html)

[**返回目錄TOP**](#content)
  
# Week4 : Insertion Sort & Quick Sort
## **About Insertion Sort**
> Insertion Sort步驟：
  
  1.從未排序的數列中取出第一項元素。
  
  2.由後往前和已排序數列中的每項元素做比較，直到遇到不大於自己的元素並插入此元素之後，若都沒有比自己小的數則插入在最前面。
  
  3.重複以上動作直到未排序數列全部處理完成。
  
   ![insertion sort](https://github.com/yuu0223/code-learning/blob/master/image/insertion%20sort.png)

## **About Quick Sort**
> Quick Sort步驟：
  
  1.在數列中任意挑選一個數(稱為pivot)，然後調整數列，比pivot小的數字都在pivot的左邊，而比pivot大的數字皆在pivot的右邊。
  
  2.接著，將所有在pivot左邊及右邊的數視為兩個「新的數列」，分別重複上述步驟(選擇新的pivot、調整數列)，直到分不出「新的數列」為止。
  
   ![quicksort](https://github.com/yuu0223/code-learning/blob/master/image/quick%20sort.png)
   
## **Reference**
* [插入排序法(Insertion Sort)](https://emn178.pixnet.net/blog/post/93791164)

* [維基百科-Quick Sort](https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F)

[**返回目錄TOP**](#content)

# Week6：Heap Sort
## **About Heap Sort**

* 堆積排序(Heap Sort)有法兩個大步驟，「最小堆積」(Min Heap)或「最大堆積」(Max Heap)。

* 如果要將陣列遞增排序的話就使用Max Heap；如果要遞減排序的話就使用Min Heap。

> Max Heap的條件：

  1 . 父節點的值大於子節點
  
  2 . 樹根(root)一定是所有節點的最大值
  
  ![heapsortmax](https://github.com/yuu0223/code-learning/blob/master/image/heap%20sort%20max.png)

> Min Heap的條件：

  1 . 父節點的值小於子節點
  
  2 . 樹根(root)一定是所有節點的最小值
  
  ![minheapsort](https://github.com/yuu0223/code-learning/blob/master/image/minheapsort.png)
  
[**返回目錄TOP**](#content)
  
# Week7：Merge Sort


[**返回目錄TOP**](#content)
