# Shortest Path

## About Shortest Path

* 旨在尋找圖（由節點和路徑組成的）中兩結點之間的最短路徑。

![sp-1](https://github.com/yuu0223/code-learning/blob/master/image/sp-1.png)

![sp-2](https://github.com/yuu0223/code-learning/blob/master/image/sp-2.png)

## Shortest Path應用 - Dijkstra演算法

* Dijkstra演算法使用了BFS(廣度優先搜尋)解決賦權有向圖的單源Shortest Path(最短路徑問題)。

* 這個演算法是通過為每個頂點 v 保留目前為止所找到的從s到v的最短路徑來工作的。

## 時間複雜度

* Dijkstra演算法：O(V^2)

## Reference
* [Shortest Path : Intro](http://alrightchiu.github.io/SecondRound/shortest-pathintrojian-jie.html)
* [維基百科 - Dijkstra演算法](https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95)
* [維基百科 - 最短路徑問題](https://zh.wikipedia.org/wiki/%E6%9C%80%E7%9F%AD%E8%B7%AF%E9%97%AE%E9%A2%98)
