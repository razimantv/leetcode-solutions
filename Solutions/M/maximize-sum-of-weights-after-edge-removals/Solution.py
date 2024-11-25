# https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def dfs(u, par):
            children = [
                [x + i * w for i, x in enumerate(dfs(v, u))]
                for v, w in adj[u] if v != par
            ]
            dp0, dp1 = 0, 0
            for i, (c0, c1) in enumerate(sorted(
                children, key=lambda p: p[0] - p[1]
            )):
                high = max(c0, c1)
                dp0 += high if i < k else c0
                dp1 += high if i < k - 1 else c0
            return dp0, dp1

        return dfs(0, -1)[0]
