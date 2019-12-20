# BFS(廣度優先搜尋) vs DFS(深度優先搜尋)

## BFS簡介

* BFS(Breadth-First Search)是從根節點開始，走完所有節點，不考慮要搜尋的值所在的位置，都要走過所有節點才能終止。按照就近原則進行，先造訪完所有相鄰的節點。

## DFS簡介

* DFS(Depth-First Search)，也是從根節點開始，逐一訪問每一條路徑，對於具有多子節點的節點而言，先搜尋到某一條子路的最深處，再回來搜尋前面的節點。

## 儲存方式
    * BFS - 利用Queue的方式儲存(先進先出)

    * DFS - 利用Stack的方式儲存(先進後出)

## 空間複雜度
    * BFS - O(V+E)

    * DFS - O(V+E)

## 造訪節點順序
    * BFS - 按照就近原則進行，先造訪完所有相鄰的節點

    * DFS - 逐一訪問每一條路徑，對於具有多子節點的節點而言，先搜尋到某一條子路的最深處，再回來搜尋前面的節點
    
## 參考資料
* [Graph: Breadth-First Search(BFS，廣度優先搜尋)](https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)
* [橫向優先搜尋 (breadth-first search)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/bfs.html)
* [BFS&DFS 學習整理](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/)
* [Depth-first search 維基百科](https://en.wikipedia.org/wiki/Depth-first_search)
* [縱向優先搜尋 (depth-first search)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dfs.html)
* [Graph: Depth-First Search(DFS，深度優先搜尋)](https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)
