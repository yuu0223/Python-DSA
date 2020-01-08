class MyQueue:

    def __init__(self):
        
        self.queue=[]

        
    def push(self, x: int) -> None:
       
        self.queue.append(x)
        

    def pop(self) -> int:
       
        return self.queue.pop(0) #pop(要移除的第n項)

    
    def peek(self) -> int:
       
        return self.queue[0]

    
    def empty(self) -> bool:
        
        return self.queue == []

#reference:https://www.runoob.com/python/python-lists.html
