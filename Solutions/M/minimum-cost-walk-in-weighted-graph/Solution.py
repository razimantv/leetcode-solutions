# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        par = list(range(n))
        compwalk = [(1 << 20) - 1] * n

        def parent(u):
            if par[u] == u:
                return u
            par[u] = parent(par[u])
            return par[u]

        for u, v, w in edges:
            u, v = parent(u), parent(v)
            compwalk[u] &= (compwalk[v] & w)
            par[v] = u

        for i, (u, v) in enumerate(query):
            if u == v:
                query[i] = 0
            else:
                u, v = parent(u), parent(v)
                query[i] = compwalk[u] if u == v else -1

        return query
