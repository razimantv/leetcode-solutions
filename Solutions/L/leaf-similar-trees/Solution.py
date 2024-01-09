# https://leetcode.com/problems/leaf-similar-trees/

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root):
            if not root:
                return []
            children = leaves(root.left) + leaves(root.right)
            return children if children else [root.val]

        return leaves(root1) == leaves(root2)
