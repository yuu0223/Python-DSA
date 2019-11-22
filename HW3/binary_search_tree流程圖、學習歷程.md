# BST流程圖

首先，為了瞭解Binary Search Tree的步驟，所以先畫了insert、delete、search、modify的流程圖：

## insert

![insert_p]()

## delete

![delete_p]()

## search

![search_p]()

## modify

![modify_p]()

# BST程式碼

再來，概念大概了解完開始試著寫寫看程式碼：

## insert

將insert程式碼分成兩個部分，第一個部分：

當root的值=None時，則直接新增val在這個位置。

```Python
def insert(self, root, val):
        if root.val == None: #若節點為none則直接新增節點的值
            newnode = TreeNode(val)
            self.root = newnode
```

第二個部分：

若root.val不等於None，則進入下面的else開始與root比較大小。

若比root小則進入左子樹的if-else中，比root大則進入右子樹的if-else。

第二層if-else中：

(1.) 右節點為none，則新增於右邊的子節點。若右子節點有值，則繼續尋找root.right下面為none的節點。

(2.) 左節點為none，則新增於左邊的子節點。若左子節點有值，則繼續尋找root.left下面為none的節點。
```Python
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
```
如此一來，insert就完成了。

# delete
delete的話，也是先分成兩個部分，第一部分：

先判斷是否為空樹，如果不是空樹，則進入第二層if-else。

進入第二層後，

(1.) root.val等於target且root.right沒有值，則將root.left上移至root的位置，就delete原始的root了。

(2.) root.val等於target且root.right有值，則進入while迴圈找出target的右子樹中最小的值(最左邊)，並將r.left上移至root的位置，就delete原始的root了。

```Python
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
```

第二部分：

然後分成兩邊(左子樹、右子樹)重複呼叫delete，分頭進行搜索target然後delete。

```Python
root.left = self.delete(root.left, target) 
root.right = self.delete(root.right, target)
#分左右邊搜尋key值，若找到則進入if root.val == key
            
   else:
        return None
        
   return root
```
delete就成功了！

# search
search也是分為兩個部分來進行，第一部分：

如果找到符合target = root.val時，就搜尋成功了。

```Python
def search(self, root, target):
        if root:
            if root.val == target: #找到值時回傳root
                return root
```

第二部分：

(1.) 當target比root.val小，則往左子樹搜尋，並再search一次。

(2.) 當target比root.val大，則往右子樹搜尋，並再search一次。
```Python
 elif target < root.val: #當target比root.val小，則往左子樹搜尋
    root = root.left
    return self.search(root, target)
                
 elif target > root.val: #當target比root.val大，則往右子樹搜尋
    root = root.right
    return self.search(root, target)
```
這樣，search就完成了。

# modify

同樣地，modify也是分成兩個部分，第一部分：

若符合target = root.val，則將新的節點(treenode(new_val))取代舊的root，modify就完成了。
```Python
 def modify(self, root, target, new_val): 
        
        r = root
        
        if target == root.val:
            newnode = TreeNode(new_val)
            r.val = newnode.val
```

第二部分：

(1.) 若target < root.val，則將root.left取代root，然後再做一次modify。

(2.) 若target > root.val，則將root.right取代root，然後再做一次modify。
```Python
elif target < root.val:
        r = r.left
        self.modify(r, target, new_val)
            
elif target > root.val:
        r = r.right
        self.modify(r, target, new_val)
```
最後，modify就完成了！

#Reference


