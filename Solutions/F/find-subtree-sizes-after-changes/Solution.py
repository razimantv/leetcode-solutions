# https://leetcode.com/problems/find-subtree-sizes-after-changes/

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i, p in enumerate(parent[1:]):
            adj[p].append(i + 1)

        last = defaultdict(list)

        def dfs(u):
            if last[s[u]]:
                parent[u] = last[s[u]][-1]

            last[s[u]].append(u)
            for v in adj[u]:
                dfs(v)
            last[s[u]].pop()
        dfs(0)

        adj = [[] for _ in range(n)]
        for i, p in enumerate(parent[1:]):
            adj[p].append(i + 1)

        ret = [0] * n

        def dfs2(u):
            ret[u] = 1
            for v in adj[u]:
                ret[u] += dfs2(v)
            return ret[u]
        dfs2(0)

        return ret
