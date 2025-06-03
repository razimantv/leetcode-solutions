# Maximum candies you can get from boxes

[Problem link](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

class Solution:
    def maxCandies(
        self, status: list[int], candies: list[int], keys: list[list[int]],
        contained: list[list[int]], initial: list[int]
    ) -> int:
        for u in initial:
            status[u] |= 2

        def dfs(u):
            ret, status[u] = candies[u], 7
            for ar, x in zip([keys[u], contained[u]], [1, 2]):
                for v in ar:
                    status[v] |= x
                    if status[v] == 3:
                        ret += dfs(v)
            return ret
        return sum(dfs(u) for u, x in enumerate(status) if x == 3)
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
