#用list node的方法
class MyLinkedList:
    class Node:
        def __init__(self, value, nextnode):
            
            self.val = value
            self.next = nextnode

            
    def __init__(self):
        
        self.head = None
        
        self.size = 0
        
        
    def get(self, index: int) -> int:
     #取得第index個點的值
        
        if index >= self.size or self.size == 0 or index < 0:
            return -1
        
        else:
            f = self.head
            i = 1
            while i <= index:
                f = f.next
                i +=1
            return f.val

        
    def addAtHead(self, val: int) -> None:
    #將值加在linked list的最前面
        
        if self.size == 0:
            newnode = self.Node(val, None)
            self.head = newnode
            self.size +=1
        
        else:
            f = self.head
            newnode = self.Node(val,f)
            self.head = newnode
            self.size +=1
            

    def addAtTail(self, val: int) -> None:
    #將值加在linked list的最尾
        
        if self.size == 0 :
            self.addAtHead(val)
            
        else:
            f = self.head
            newnode = self.Node(val,None)
            while f.next != None:
                f = f.next
            f.next = newnode
            self.size +=1
                
        

    def addAtIndex(self, index: int, val: int) -> None:
    #在第index個點加入某值，如果index = 鍊錶長度，則加在尾端；若index > 練表長度，則不執行
        
        if index == self.size and index > 0:
            self.addAtTail(val)
        
        elif index > self.size:
            return
        
        elif index == 0:
            f = self.head
            newnode = self.Node(val,f)
            self.head = newnode
            self.size +=1
        
        else:
            f = self.head
            i = 1
            while i <= index:
                f_last = f
                #插入位置的前一項
                f = f.next
                #插入位置的後一項
                i +=1
            f_last.next = self.Node(val, f)
            self.size +=1
        

    def deleteAtIndex(self, index: int) -> None:
    #如果索引有效，則將第index的值刪除
    
        if index < 0 or index >= self.size or self.size == 0:
            return
        
        elif index == 0 :
            f = self.head
            self.head = f.next
            self.size -=1
        
        else:
            f = self.head
            i = 1
            while i <= index:
                f_last = f
                f = f.next
                i +=1
            f_last.next = f.next
            self.size -=1
                
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

#Ref. https://www.itread01.com/content/1544792077.html
