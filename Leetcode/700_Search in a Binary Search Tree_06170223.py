class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root:
            if root.val == val:
                return root
            
            if val < root.val:
                root = root.left
                return self.searchBST(root, val)
                
            elif val > root.val:
                root = root.right
                return self.searchBST(root, val)
                
        else:
            return
            
#reference:https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9
