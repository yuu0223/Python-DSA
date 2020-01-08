class Solution:
    class TreeNode:
        def __init__(self, value):
            self.val = value
            self.left = None
            self.right = None
        
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    #新增
        
        if root.val == None:
            newnode = TreeNode(val)
            self.root = newnode
            
        else:
            if val > root.val:
                if root.right == None:
                    newnode = TreeNode(val)
                    root.right = newnode
                    
                else:
                    self.insertIntoBST(root.right, val)
                    
            if val < root.val:
                if root.left == None:
                    newnode = TreeNode(val)
                    root.left = newnode
                    
                else:
                    self.insertIntoBST(root.left, val)
                    
            return root
            
#reference:https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9
