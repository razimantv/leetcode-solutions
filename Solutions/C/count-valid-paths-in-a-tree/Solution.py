# https://leetcode.com/problems/count-valid-paths-in-a-tree/

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        notprime = [0] * (n+1)
        notprime[1] = 1
        for i in range(2, n+1):
            if i*i > n:
                break
            if notprime[i]:
                continue
            for j in range(i*i, n+1, i):
                notprime[j] = 1

        ret = 0

        def dfs(u, par):
            nonlocal ret
            path0 = notprime[u]
            path1 = 1-path0

            for v in adj[u]:
                if v == par:
                    continue
                c0, c1 = dfs(v, u)
                ret += path0 * c1 + path1 * c0
                path0 += notprime[u] * c0
                path1 += notprime[u] * (c1 - c0) + c0
            return path0, path1

        dfs(1, 0)
        return ret
