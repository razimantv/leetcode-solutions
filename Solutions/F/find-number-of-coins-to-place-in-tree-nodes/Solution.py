# https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ret = [0] * n

        def dfs(u, par):
            cnt, ar = 1, [cost[u]]
            for v in adj[u]:
                if v == par:
                    continue
                ccnt, car = dfs(v, u)
                cnt += ccnt
                ar += car

            ar = sorted(ar)
            if cnt < 3:
                ret[u] = 1
                return cnt, ar

            if len(ar) > 6:
                ar = ar[:3] + ar[-3:]
            best = 0
            for i in range(len(ar)):
                for j in range(i):
                    for k in range(j):
                        best = max(best, ar[i] * ar[j] * ar[k])
            ret[u] = best
            return cnt, ar

        dfs(0, -1)
        return ret
