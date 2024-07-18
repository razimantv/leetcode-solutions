# Number of good leaf nodes pairs

[Problem link](https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def work(root):
            ret, count = 0, [0] * distance
            if not root. left and not root.right:
                count[0] = 1
                return ret, count
            for child in [root.left, root.right]:
                if not child:
                    continue
                cret, ccount = work(child)
                ret += cret
                pref = 0
                for i in range(distance-1, -1, -1):
                    pref += count[distance - 1 - i]
                    ret += ccount[i] * pref
                for i in range(distance-1):
                    count[i+1] += ccount[i]
            return ret, count
        return work(root)[0]
```
## Tags

* [Dynamic programming](/README.md#Dynamic_programming) > [Trees](/README.md#Dynamic_programming-Trees) > [DP over children](/README.md#Dynamic_programming-Trees-DP_over_children)
* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum)
