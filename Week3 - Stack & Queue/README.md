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
