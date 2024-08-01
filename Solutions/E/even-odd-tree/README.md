# Even odd tree

[Problem link](https://leetcode.com/problems/even-odd-tree/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/even-odd-tree/

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def work(root, level, vals):
            if not root:
                return True
            elif (root.val ^ level) & 1:
                return False
            elif len(vals) == level:
                vals.append(root.val)
            elif (root.val - vals[level]) * (2 * (level & 1) - 1) <= 0:
                return False
            else:
                vals[level] = root.val
            return work(
                root.left, level + 1, vals
            ) and work(
                root.right, level + 1, vals
            )
        return work(root, 1, [None])
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
