# Dijkstra Algorithm (戴克斯特拉演算法) & Kruskal Algorithm (克魯斯克爾演算法)

## About Dijkstra

* Dijkstra使用了廣度優先搜尋(BFS)解決賦權有向圖的單源最短路徑問題(shortest path)，主要是利用兩點間的權重路徑，找出各點距離起點的最短路徑。

* Step 步驟：
       

## About Kruskal

* Kruskal是一種用來尋找最小生成樹(minimum spanning tree)的演算法。

* Step 步驟：

       1. 將原圖中所有的路徑權重按權值從小到大排序
              
       2. 從權值最小的路徑開始，依路徑把兩個節點連結起來
       
       3. 重複步驟2，直至所有的節點都連過了
       
## 時間複雜度

      * Dijkstra - O( |E|+|V|log|V| )
      
      * Kruskal - O( |E|log|V| )

## Reference
* [維基百科 - Dijkstra](https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95)
* [維基百科 - Kruskal](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)
* [代克思托演算法 (Dijkstra's algorithm)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html)
* [上課ppt](https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.g7b9afdb0e7_0_4)
