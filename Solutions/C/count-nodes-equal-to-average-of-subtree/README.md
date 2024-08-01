# Count nodes equal to average of subtree

[Problem link](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

import numpy as np


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def work(root):
            ret = np.array([0, root.val, 1])
            for child in [root.left, root.right]:
                if child:
                    ret += work(child)
            if ret[1] // ret[2] == root.val:
                ret[0] += 1
            return ret
        return work(root)[0]
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Averaging from total and count](/Collections/averaging-from-total-and-count.md#averaging-from-total-and-count)
