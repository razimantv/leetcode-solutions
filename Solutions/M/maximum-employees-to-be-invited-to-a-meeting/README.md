# Maximum employees to be invited to a meeting

[Problem link](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting

class Solution:
    def maximumInvitations(self, favourite: list[int]) -> int:
        n = len(favourite)
        seen, twos, adj = [-1] * n, {}, defaultdict(list)
        for i, u in enumerate(favourite):
            adj[u].append(i)

        def cycle(u):
            i, stk, cur = u, [], 1
            while seen[u] == -1:
                stk.append(u)
                seen[u] = i
                u = favourite[u]
            if seen[u] == i:
                if stk[-2] == u:
                    twos.update({u: 0, stk[-1]: 0})
                while stk[-1] != u:
                    stk.pop()
                    cur += 1
            return cur

        def dfs(u):
            return max((dfs(v) for v in adj[u]), default=0) + 1

        ret = max(cycle(i) for i in range(n) if seen[i] == -1)
        for u, v in enumerate(favourite):
            if v in twos and u not in twos:
                twos[v] = max(twos[v], dfs(u))
        return max(ret, sum(x + 1 for u, x in twos.items()))
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Single outdegree graphs](/Collections/graph-theory.md#single-outdegree-graphs)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Cycle detection](/Collections/graph-theory.md#cycle-detection)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Reuse visited array](/Collections/graph-theory.md#reuse-visited-array)
* [Stack](/Collections/stack.md#stack)
