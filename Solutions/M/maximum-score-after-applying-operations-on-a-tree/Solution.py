# https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(u, par):
            ret = values[u]
            children = []
            for v in adj[u]:
                if v == par:
                    continue
                children.append(dfs(v, u))
            if children:
                ret = min(ret, sum(children))
            return ret

        return sum(values) - dfs(0, -1
