# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        N = m * n
        adj, seen = [[] for _ in range(N)], [0] * N
        for i in range(m):
            for j in range(n):
                u = i * n + j
                if j and grid[i][j - 1] in [1, 4, 6] and grid[i][j] in [1, 3, 5]:
                    adj[u]. append(u - 1)
                    adj[u - 1]. append(u)
                if i and grid[i - 1][j] in [2, 3, 4] and grid[i][j] in [2, 5, 6]:
                    adj[u]. append(u - n)
                    adj[u - n]. append(u)

        def dfs(u):
            if not u:
                return True
            seen[u] = 1
            for v in adj[u]:
                if not seen[v] and dfs(v):
                    return True
            return False
        return dfs(N-1)
