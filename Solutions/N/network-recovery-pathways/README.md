# Network recovery pathways

[Problem link](https://leetcode.com/problems/network-recovery-pathways/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/network-recovery-pathways/

class Solution:
    def findMaxPathScore(
        self, edges: list[list[int]], online: list[bool], k: int
    ) -> int:
        n = len(online)

        def work(x):
            adj = [[] for _ in range(n)]
            for u, v, w in edges:
                if w >= x:
                    adj[u].append((v, w))
            
            @cache
            def dist(u):
                if u == n - 1:
                    return 0
                elif not online[u]:
                    return inf
                else:
                    return min((
                        w + dist(v) for (v, w) in adj[u]
                    ), default=inf)
            
            return dist(0) <= k

        start, end = -1, max((w for u, v, w in edges), default=10 ** 9) + 1
        while end - start > 1:
            mid = (start + end) // 2
            if work(mid):
                start = mid
            else:
                end = mid
        return start
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Directed acyclic graph](/Collections/graph-theory.md#directed-acyclic-graph)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
