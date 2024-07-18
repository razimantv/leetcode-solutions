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
