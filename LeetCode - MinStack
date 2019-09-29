class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items=[]
        self.items_min=[] #為了取得最小值所設
        

    def push(self, x: int) -> None:
        
        self.items.append(x)
        
        if len(self.items_min) == 0 or x <= self.items_min[-1]:
            self.items_min.append(x) 
            #若最小值的list中無值可比較or輸入的x比item_min list中的數值小，則append
        
    def pop(self) -> None:
        
        top = self.items[-1] #先設置top為哪一個list的
        self.items.pop() 
    
        if top == self.items_min[-1]: 
            self.items_min.pop()
            #若items_min和items list中最後一項相同則須移除
       

    def top(self) -> int:
        
        return self.items[-1] #列出最後一項
        

    def getMin(self) -> int:
        
        return self.items_min[-1] #列出items_min的最後一項取得最小值
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
