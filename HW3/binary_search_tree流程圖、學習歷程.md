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

將insert程式碼分成三個部分，第一個部分：

當root的值=None時，則直接新增val在這個位置。

```Python
class Solution(object):
    def insert(self, root, val):
        if root.val == None: #若節點為none則直接新增節點的值
            newnode = TreeNode(val)
            self.root = newnode
```

第二個部分：

若root.val不等於None，則進入下面的else開始與root比較大小。

若比root小則進入左子樹的if-else中，比root大則進入右子樹的if-else。

第二層if-else中，右(左)節點為none，則新增於右(左)邊的子節點。若右(左)子節點有值，則繼續尋找root.right(root.left)下面為none的節點。

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



```Python
def delete(self, root, target):
        if root: #如果有root
            
            if root.val == target: #如果root的value = key值
                
                if not root.right: #如果root沒有右子項，則直接將左子項移上來
                    move = root.left
                    return move
```

