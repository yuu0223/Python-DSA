#利用list方法來寫的linked list
class MyLinkedList:

    def __init__(self):
        
        self.linked_list = list()

    def get(self, index: int) -> int:
    #取得第index個點的值
        
        if len(self.linked_list) <= index or index < 0 :
            return -1
        else:
            return self.linked_list[index]
        

    def addAtHead(self, val: int) -> None:
    #將值加在linked list的最前面
        
        self.linked_list.insert(0,val)
        
        

    def addAtTail(self, val: int) -> None:
    #將值加在linked list的最尾端
    
        self.linked_list.append(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
    #在第index個點加入某值，如果index = 鍊錶長度，則加在尾端；若index > 練表長度，則不執行
        
        if index == len(self.linked_list):
            self.linked_list.append(val)
            
        elif index > len(self.linked_list):
            return
        
        else:
            self.linked_list.insert(index,val)
        

    def deleteAtIndex(self, index: int) -> None:
    #如果索引有效，則將第index的值刪除掉
        
        if index >= len(self.linked_list) or index < 0:
            return
        
        else:
            self.linked_list.pop(index)
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
