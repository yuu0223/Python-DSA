 
from collections import defaultdict 

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list) 

        
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    
    def BFS(self, s):
        
        store = [] #暫存的list
        sure = [] #確定的list
        
        for a in range(len(self.graph)): #self.graph的長度=要排序的個數
            if s not in store:
                    if s not in sure:
                        store.append(s) #若s皆不在暫存及確定的list中則新增進暫存的list
        
            for i in self.graph[s]: #[s]的位置上可能不只一個數,利用for迴圈一個一個讀出
                if i not in store:
                    if i not in sure:
                        store.append(i) #一個一個新增進暫存的list
        
            sure.append(s)
            store.pop(0) #將新增進確定的list從暫存區刪除
           
        
            if len(sure) == len(self.graph): #sure的個數=self.graph個數代表已經排序好
                return sure
            
            else:
                s = store[0] 
                
                
    def DFS(self, s):
        
        stack = []
        sure = []
        i = 1
        
        while len(sure) != len(self.graph):
            
            if s not in sure:
                sure.append(s)
                    
            stack = self.graph[s]
            
            if stack == []: #若stack是空的就從sure中往回推一個元素
                node = sure[-1-i]
                i+=1
                stack = self.graph[node]
                
            else:
                node = stack[-1]
            
            if node not in sure:
                sure.append(node)
                stack.pop()
                
            else:
                if stack !=[]: #若該點的stack不是空的
                    if stack[-1] not in sure: #若stack最上層的元素不在sure中
                        node = stack[-1]
                    
                    else:
                        stack.pop() #若在就直接從stack中刪除掉
            
            
            s = node #令下一個s為node
            
        return sure

      
#Reference - BFS:
#https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
#http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/bfs.html
#https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7aa022d8bc_2_0

#Reference - DFS:
#https://en.wikipedia.org/wiki/Depth-first_search
#http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dfs.html
#https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
