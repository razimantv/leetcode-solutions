# https://leetcode.com/problems/balance-a-binary-search-tree/

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root, ar):
            if not root:
                return
            inorder(root. left, ar)
            ar. append(root. val)
            inorder(root. right, ar)

        ar = []
        inorder(root, ar)

        def balanced(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            return TreeNode(ar[m], balanced(l, m - 1), balanced(m+1, r))

        return balanced(0, len(ar) - 1)
