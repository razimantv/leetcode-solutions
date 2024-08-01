# Find the city with the smallest number of neighbors at a threshold distance

[Problem link](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], threshold: int
    ) -> int:
        dist = [[threshold + 1] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = min(dist[u][v], w)
            dist[v][u] = dist[u][v]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        best, bestcnt = -1, n
        for i in range(n):
            cur = sum(x <= threshold for x in dist[i])
            if cur <= bestcnt:
                best, bestcnt = i, cur
        return best
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Floyd-Warshall algorithm](/Collections/graph-theory.md#floyd-warshall-algorithm)
