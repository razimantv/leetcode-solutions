# https://leetcode.com/problems/regions-cut-by-slashes/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        conv = {'/': ['UL', 'DR'], '\\': ['UR', 'DL'], ' ': ['ULDR']}
        par = {}

        def parent(u):
            if u not in par:
                par[u] = u
            elif par[u] != u:
                par[u] = parent(par[u])
            return par[u]

        def merge(u, v):
            u, v = parent(u), parent(v)
            if u != v:
                par[u] = v
                return 1
            return 0

        def node(i, j, c):
            for part in conv[grid[i][j]]:
                if c in part:
                    return (i, j, part)

        components = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                components += len(conv[grid[i][j]])
                if i:
                    components -= merge(node(i, j, 'U'), node(i-1, j, 'D'))
                if j:
                    components -= merge(node(i, j, 'L'), node(i, j - 1, 'R'))
        return components
