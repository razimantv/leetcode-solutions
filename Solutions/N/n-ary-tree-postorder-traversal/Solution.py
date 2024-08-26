# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def work(node, order):
            if not node:
                return
            for child in node.children:
                work(child, order)
            order.append(node.val)
            return order
        return work(root, [])
