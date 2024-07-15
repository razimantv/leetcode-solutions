# https://leetcode.com/problems/create-binary-tree-from-descriptions/

class Solution:
    def createBinaryTree(
        self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        seen = {}

        def node(x):
            if x not in seen:
                seen[x] = TreeNode(x)
            return seen[x]

        csum = 0
        for u, v, left in descriptions:
            if left:
                node(u).left = node(v)
            else:
                node(u).right = node(v)
            csum += v
        root = sum(u.val for u in seen.values()) - csum
        return seen[root]
