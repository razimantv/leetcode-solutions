# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        def work(root, level):
            if not root:
                return
            if level == len(ret):
                ret.append(root.val)
            else:
                ret[level] = max(ret[level], root.val)
            work(root.left, level+1)
            work(root.right, level+1)
        work(root, 0)
        return ret
