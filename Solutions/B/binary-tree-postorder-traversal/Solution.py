# https://leetcode.com/problems/binary-tree-postorder-traversal/

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def work(node, order):
            if not node:
                return
            for child in [node.left, node.right]:
                work(child, order)
            order.append(node.val)
        order = []
        work(root, order)
        return order
