# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        values = set()

        def work(node, x):
            values.add(x)
            node.val = x
            if node.left:
                work(node.left, 2 * x + 1)
            if node.right:
                work(node.right, 2 * x + 2)
        work(root, 0)
        self.values = values

    def find(self, target: int) -> bool:
        return target in self.values
