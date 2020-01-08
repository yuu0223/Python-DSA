class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if root: #如果有root
            
            if root.val == key: #如果root的value = key值
                
                if not root.right: #如果root沒有右子項，則直接將左子項移上來
                    move = root.left
                    return move
                
                else: #root有右子項，但左子項可有可無
                    r = root.right
                    
                    while r.left: #將欲刪除的節點下面右節點的左子項移上來至root(右邊最左邊的節點為比root大中最小的值)
                        r = r.left
                        
                    #交換位置
                    move = root.val
                    root.val = r.val
                    r.val = move
                
            root.left = self.deleteNode(root.left, key) 
            root.right = self.deleteNode(root.right, key)
            #分左右邊搜尋key值，若找到則進入if root.val == key
            
        else:
            return None
        
        return root
        
#reference:https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9
