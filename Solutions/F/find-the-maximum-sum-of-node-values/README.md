# Find the maximum sum of node values

[Problem link](https://leetcode.com/problems/find-the-maximum-sum-of-node-values/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

class Solution:
    def maximumValueSum(
        self, nums: List[int], k: int, edges: List[List[int]]
    ) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(u, par):
            odd, even = nums[u] ^ k, nums[u]
            for v in adj[u]:
                if v == par:
                    continue
                codd, ceven = dfs(v, u)
                odd, even = max(odd + ceven, even +
                                codd), max(odd + codd, even + ceven)
            return odd, even

        return dfs(0, -1)[1]
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees) > [DP over children](/Collections/dynamic-programming.md#dp-over-children)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
