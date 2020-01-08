# Depth-First Search(深度優先搜尋)

## About DFS

* DFS(Depth-First Search)，也是從根節點開始，逐一訪問每一條路徑，對於具有多子節點的節點而言，先搜尋到某一條子路的最深處，再回來搜尋前面的節點。

## DFS步驟

    (1.) 首先將根節點放入stack中。
    
    (2.) 從stack中取出第一個節點，並檢驗它是否為目標。如果找到目標，則結束搜尋並回傳結果。否則將它某一個尚未檢驗過的直接子節點加入stack中。
  
    (3.) 重複步驟2。
    
    (4.) 如果不存在未檢測過的直接子節點。將上一級節點加入stack中。重複步驟2。
  
    (5.) 重複步驟4。

    (6.) 若stack為空，表示整張圖都檢查過了——亦即圖中沒有欲搜尋的目標。結束搜尋並回傳「找不到目標」。

## 時間複雜度

* 時間複雜度：O(b^m)

## 空間複雜度

* 空間複雜度：O(bm)

## Reference
* [維基百科 - 深度優先搜尋](https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)
* [Graph: Depth-First Search(DFS，深度優先搜尋)](https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)
