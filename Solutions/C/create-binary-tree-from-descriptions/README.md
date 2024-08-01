# Create binary tree from descriptions

[Problem link](https://leetcode.com/problems/create-binary-tree-from-descriptions/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/create-binary-tree-from-descriptions/

class Solution:
    def createBinaryTree(
        self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        seen = {}

        def node(x):
            if x not in seen:
                seen[x] = TreeNode(x)
            return seen[x]

        csum = 0
        for u, v, left in descriptions:
            if left:
                node(u).left = node(v)
            else:
                node(u).right = node(v)
            csum += v
        root = sum(u.val for u in seen.values()) - csum
        return seen[root]
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree)
