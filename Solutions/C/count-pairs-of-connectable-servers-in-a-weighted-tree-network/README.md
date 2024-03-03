# Count pairs of connectable servers in a weighted tree network

[Problem link](https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

class Solution:
    def countPairsOfConnectableServers(
        self, edges: List[List[int]], signalSpeed: int
    ) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))

        def dfs(u, par, pref):
            ret = not pref
            for v, w in adj[u]:
                if v == par:
                    continue
                ret += dfs(v, u, (pref + w) % signalSpeed)
            return ret

        def work(u):
            ret, tot = 0, 0
            for v, w in adj[u]:
                cur = dfs(v, u, w % signalSpeed)
                ret += tot * cur
                tot += cur
            return ret

        return [work(u) for u in range(n)]
```
## Tags

* [Dynamic programming](/README.md#Dynamic_programming) > [Trees](/README.md#Dynamic_programming-Trees) > [DP over children](/README.md#Dynamic_programming-Trees-DP_over_children)
* [Graph theory](/README.md#Graph_theory) > [Depth first search](/README.md#Graph_theory-Depth_first_search)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
