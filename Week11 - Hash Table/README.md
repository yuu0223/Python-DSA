# Week11 - Hash Table
## About Hash(雜湊)

* 一種對資料的處理方法，通過某種特定的函式/演算法，將要檢索的value與用來檢索的key(稱為雜湊or雜湊值)關聯起來，形成一個便於搜尋的資料結構(稱為雜湊表)。

* Hash並不是加密，是他的特性很適合拿來做加密的運算。

## About Hash Function(雜湊函數)

* 將各個長度不一樣的訊息輸入後，演算成長度固定的Hash值輸出，且計算出的雜湊值需符合以下兩點：
     
      1. 由Hash後的值不能反推回原本的訊息
      
      2. Hash值須隨明文改變而改變
      
## About Hash Table(雜湊表)

* 用Hash Function運算出來的雜湊值，根據key來儲存在Hash Table中。而存放這些記錄的數組就稱為Hash Table(雜湊表)。

* 每一個Hash Table裡都有n個bucket，而每個bucket裡也有n個slot。(n自行定義)

![hash_table](https://github.com/yuu0223/code-learning/blob/master/image/hash_table.jpg)

## Reference
* [資料結構-雜湊 (Hash)](https://ithelp.ithome.com.tw/articles/10208884)
* [Hash Table:Intro(簡介)](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html#ht)
* [維基百科-Hash](https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97)
