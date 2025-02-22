# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)

        def get(i):
            d, v = 0, 0
            while traversal[i] == '-':
                i, d = i + 1, d + 1
            while i < n and (c := traversal[i]) != '-':
                i, v = i + 1, v * 10 + int(c)
            return i, d, v

        i, stack = 0, []
        while i < n:
            i, d, v = get(i)
            while len(stack) > d:
                stack.pop()
            node = TreeNode(v)
            if stack:
                if stack[-1].left:
                    stack[-1].right = node
                else:
                    stack[-1].left = node
            stack.append(node)
        return stack[0]
