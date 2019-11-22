class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
        if root.val == None: #若節點為none則直接新增節點的值
            newnode = TreeNode(val)
            self.root = newnode
            
        else:
            if val > root.val: #若值大於root的值
                if root.right == None: #且右節點為none，則新增於右邊的子節點
                    newnode = TreeNode(val)
                    root.right = newnode
                    
                else:
                    self.insert(root.right, val) #若右子節點有值，則繼續尋找root.right下面為none的節點
                    
            if val < root.val: #若值小於root的值
                if root.left == None: #且左子節點為none，則新增於左邊的子節點
                    newnode = TreeNode(val)
                    root.left = newnode
                    
                else:
                    self.insert(root.left, val) #若左子節點有值，則繼續尋找root.left下面為none的節點
                    
            return root
    
    def delete(self, root, target):
        if root: #如果有root
            
            if root.val == target: #如果root的value = key值
                
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
                
            root.left = self.delete(root.left, target) 
            root.right = self.delete(root.right, target)
            #分左右邊搜尋key值，若找到則進入if root.val == key
            
        else:
            return None
        
        return root
     
    def search(self, root, target):
        if root:
            if root.val == target: #找到值時回傳root
                return root
            
            elif target < root.val: #當target比root.val小，則往左子樹搜尋
                root = root.left
                return self.search(root, target)
                
            elif target > root.val: #當target比root.val大，則往右子樹搜尋
                root = root.right
                return self.search(root, target)
                
        else: #若找不到則回傳空白
            return
       
    def modify(self, root, target, new_val): 
        
        r = root
        
        if target == root.val:
            newnode = TreeNode(new_val)
            r.val = newnode.val
        
        elif target < root.val:
            r = r.left
            self.modify(r, target, new_val)
            
        elif target > root.val:
            r = r.right
            self.modify(r, target, new_val)
        
        else:
            return
        
        return root
    
#Ref1: 維基百科 - 二元搜尋樹 https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9
#Ref2: 資料結構 https://medium.com/@Kadai/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E5%A4%A7%E4%BE%BF%E7%95%B6-binary-search-tree-3c40be3204e
#Ref3: 老師上課ppt https://docs.google.com/presentation/d/e/2PACX-1vQgUh73yvSdxAvMH50DHWJ5lsCX8-daMxtoltU9rYW7xCmqYz2A1wOv0Vcx_F9KO5ZUvZBv3IF1TjGi/pub?start=false&loop=false&delayms=3000&slide=id.g659a558647_1_0
                
