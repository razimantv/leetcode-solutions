# https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

class Solution:
    def numberOfSets(
        self, n: int, maxDistance: int, roads: List[List[int]]
    ) -> int:
        adj = [[10**9] * n for _ in range(n)]
        for i in range(n):
            adj[i][i] = 0
        for u, v, w in roads:
            adj[u][v] = min(adj[u][v], w)
            adj[v][u] = min(adj[v][u], w)

        def good(mask):
            verts = []
            for i in range(n):
                if mask & (1 << i):
                    verts.append(i)

            m = len(verts)
            dist = [[adj[u][v] for v in verts] for u in verts]
            for k in range(m):
                for i in range(m):
                    for j in range(m):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

            for row in dist:
                if max(row) > maxDistance:
                    return False
            return True

        return len([mask for mask in range(1 << n) if good(mask)])
