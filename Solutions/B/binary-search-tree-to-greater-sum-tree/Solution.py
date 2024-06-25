# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def work(root, add):
            if not root:
                return add
            add = work(root.right, add)
            root.val += add
            add = root.val
            return work(root.left, add)

        work(root, 0)
        return root
