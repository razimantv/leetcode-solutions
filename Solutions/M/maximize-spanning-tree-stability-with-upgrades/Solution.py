# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        edges = sorted(edges, key=lambda x: (-x[3], -x[2]))
        minmust = min(
            (edge[2] for edge in edges if edge[3] == 1),
            default=200000
        )

        def poss(x):
            par = list(range(n))

            def parent(u):
                if par[u] == u:
                    return u
                par[u] = parent(par[u])
                return par[u]

            components, kleft = n, k
            for u, v, s, must in edges:
                pu, pv = parent(u), parent(v)
                if pu == pv:
                    if must:
                        return False
                    continue

                if 2 * s < x or (s < x and not kleft):
                    continue
                if s < x:
                    kleft -= 1
                par[pu] = pv
                components -= 1

            return components == 1

        start, end = -1, minmust + 1
        while end - start > 1:
            mid = (start + end) // 2
            if poss(mid):
                start = mid
            else:
                end = mid
        return start
