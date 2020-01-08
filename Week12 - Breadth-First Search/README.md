# Breadth-First Search(廣度優先搜尋)

## About BFS

* BFS(Breadth-First Search)是從根節點開始，走完所有節點，不考慮要搜尋的值所在的位置，都要走過所有節點才能終止。按照就近原則進行，先造訪完所有相鄰的節點，才到下一層的節點。

![bfs](https://github.com/yuu0223/code-learning/blob/master/image/bfs-ex.png)

## BFS步驟

      (1.) 選擇一個節點當作起點

      (2.) 造訪該節點的所有鄰節點

      (3.) 確定造訪過的節點則加進確定的list中

      (4.) 重複步驟2、3直至所有節點都在確定的list中

## 時間複雜度

* 最差情形下，BFS必須尋找所有到可能節點的所有路徑，因此其時間複雜度為 O(|V|+|E|)，其中|V|是節點的數目，而|E|是圖中邊的數目。

## 空間複雜度

* 因為所有節點都必須被儲存，因此其空間複雜度為 O(|V|+|E|)，其中|V|是節點的數目，而|E|是圖中邊的數目。

## Reference
* [Graph: Breadth-First Search(BFS，廣度優先搜尋)](https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)
* [維基百科 - 廣度優先搜尋](https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)
