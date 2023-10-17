# https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, left: List[int], right: List[int]) -> bool:
        degree = [0] * n
        for x in left+right:
            if x == -1:
                continue
            if degree[x]:
                return False
            degree[x] = 1
        roots = [i for i in range(n) if not degree[i]]
        if len(roots) != 1:
            return False
        seen = [False] * n

        def dfs(u):
            seen[u] = True
            for v in [left[u], right[u]]:
                if v != -1:
                    dfs(v)
        dfs(roots[0])

        return len([u for u in range(n) if not seen[u]]) == 0
