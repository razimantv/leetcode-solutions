# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        def graph(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return n, adj
        n1, adj1 = graph(edges1)
        n2, adj2 = graph(edges2)

        def distances(n, adj, lmax):
            def dfs(u, par, d):
                if d > lmax:
                    return 0
                return 1 + sum(dfs(v, u, d + 1) for v in adj[u] if v != par)
            return [dfs(u, -1, 0) for u in range(n)]

        cnt1 = distances(n1, adj1, k)
        cnt2max = max(distances(n2, adj2, k - 1))
        return [x + cnt2max for x in cnt1]
