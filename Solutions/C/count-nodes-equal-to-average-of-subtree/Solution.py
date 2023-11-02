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
