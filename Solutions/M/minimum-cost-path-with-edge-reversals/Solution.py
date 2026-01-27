# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u]. append((v, w))
            adj[v]. append((u, 2 * w))

        dist, djset = {0: 0}, SortedList([(0, 0)])
        while djset:
            d, u = djset.pop(0)
            for v, w in adj[u]:
                if v in dist and dist[v] > d + w:
                    djset.remove((dist[v], v))
                    dist.pop(v)
                if v not in dist:
                    dist[v] = d + w
                    djset.add((d + w, v))

        return dist.get(n - 1, -1)
