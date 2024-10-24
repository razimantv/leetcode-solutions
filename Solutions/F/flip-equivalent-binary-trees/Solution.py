# https://leetcode.com/problems/flip-equivalent-binary-trees/

class Solution:
    def flipEquiv(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        def vec(root):
            if not root: 
                return [-1]
            lc, rc = vec(root.left), vec(root.right)
            return [root.val] + sorted([lc, rc])
        return vec(root1) == vec(root2)
