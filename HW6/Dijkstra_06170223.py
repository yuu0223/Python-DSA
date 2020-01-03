from collections import defaultdict 
 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
      
      
    def Dijkstra(self, s): 
        
        sure = {}
        sure_num = []
        
        sure[s] = self.graph[s] #將起始點加進sure
        sure_num.append(s) #將起始點也新增近sure_num
        
        last = sure[s] #直至上一個數字的路徑數
        
        def add(s):
 
            for a in range(len(self.graph)):
                if self.graph[s][a] != 0 and a not in sure_num: #找出和該點有連結的所有點

                    second = last[s] + self.graph[s][a] #該點走至下一個點的路徑數
                    
                    if last[a] == 0:
                        last[a] = second

                    elif second < last[a]: #若路徑數比之前所儲存的還小則取代之前的
                        last[a] = second

            sure[s] = last
            sure_num.append(s)
            
        
        while len(self.graph) != len(sure_num):
            find_min = max(last)
            for i in range(len(self.graph)): #尋找下一個節點
                if last[i] != 0 and i not in sure_num: #確定過的數字則不用再找
                    if last[i] < find_min:
                        find_min = last[i]
                    
            s = last.index(find_min)
            
            add(s)
            
        
        ans = {}
        for i in range(len(self.graph)):
            ans[str(i)] = sure[s][i]
            
        return ans
       
       
