首先，為了瞭解Binary Search Tree的步驟，所以先畫了insert、delete、search、modify的流程圖：

* insert

![insert_p]()

* delete

![delete_p]()

* search

![search_p]()

* modify

![modify_p]()

再來，概念大概了解完開始試著寫寫看程式碼：

* insert

```Python
class Solution(object):
    def insert(self, root, val):
        if root.val == None: #若節點為none則直接新增節點的值
            newnode = TreeNode(val)
            self.root = newnode
```
