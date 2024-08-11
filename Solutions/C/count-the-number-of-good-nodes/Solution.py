# https://leetcode.com/problems/count-the-number-of-good-nodes/

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(len(edges) + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(u, par):
            cnt, size, csize, good = 0, 1, -1, True
            for v in adj[u]:
                if v == par:
                    continue
                ccnt, ncsize = dfs(v, u)
                cnt, size = cnt + ccnt, size + ncsize
                if csize == -1:
                    csize = ncsize
                elif csize != ncsize:
                    good = False
            return cnt + good, size

        return dfs(0, -1)[0]
