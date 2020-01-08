# Minimum Spanning Tree

## About MST

* 最小生成樹是一副連通加權無向圖中一棵權值最小的生成樹。一個連通圖可能有多個生成樹。當圖中的邊具有權值時，總會有一個生成樹的邊的權值之和小於或者等於其它生成樹的邊的權值之和。廣義上而言，對於非連通無向圖來說，它的每一連通分量同樣有最小生成樹，它們的並被稱為最小生成森林。

![mst](https://github.com/yuu0223/code-learning/blob/master/image/mst.png)

## MST應用 - Kurskal演算法

* Kruskal演算法是一種用來尋找最小生成樹的演算法

* Kruskal步驟：

      (1.) 新建圖G，G中擁有原圖中相同的節點，但沒有邊
      
      (2.) 將原圖中所有的邊按權值從小到大排序
      
      (3.) 從權值最小的邊開始，如果這條邊連接的兩個節點於圖G中不在同一個連通分量中，則添加這條邊到圖G中
      
      (4.) 重複3，直至圖G中所有的節點都在同一個連通分量中

![kruskal](https://github.com/yuu0223/code-learning/blob/master/image/mst-kruskal.gif)
