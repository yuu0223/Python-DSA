class MinStack:

    def __init__(self):
        
        self.stack=[]
        self.minstack=[] #為了取得最小值所設
        

    def push(self, x: int) -> None:
        
        self.stack.append(x)
        
        if len(self.minstack) == 0 or x <= self.minstack[-1]:
            self.minstack.append(x) 
            #若最小值的list中無值可比較or輸入的x比item_min list中的數值小，則append
        
    def pop(self) -> None:
        
        top = self.stack[-1] #先設置top為哪一個list的
        self.stack.pop() 
    
        if top == self.minstack[-1]: 
            self.minstack.pop()
            #若items_min和items list中最後一項相同則須移除
       

    def top(self) -> int:
        
        return self.stack[-1] #列出最後一項
        

    def getMin(self) -> int:
        
        return self.minstack[-1] #列出items_min的最後一項取得最小值
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#reference:https://www.runoob.com/python/python-lists.html
