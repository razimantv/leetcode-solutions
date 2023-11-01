# Find mode in binary search tree

[Problem link](https://leetcode.com/problems/find-mode-in-binary-search-tree/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-mode-in-binary-search-tree/

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = defaultdict(int)

        def recurse(root):
            if not root:
                return
            cnt[root.val] += 1
            recurse(root.left)
            recurse(root.right)

        recurse(root)
        maxcnt = max(v for k, v in cnt.items())
        return [k for k, v in cnt.items() if v == maxcnt]
```
## Tags

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
* [Hashmap](/README.md#Hashmap)
