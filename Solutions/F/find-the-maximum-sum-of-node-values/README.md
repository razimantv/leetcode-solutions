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

* [Bitwise operation](/README.md#Bitwise_operation) > [Self-inverse property of xor](/README.md#Bitwise_operation-Self_inverse_property_of_xor)
* [Dynamic programming](/README.md#Dynamic_programming) > [Trees](/README.md#Dynamic_programming-Trees) > [DP over children](/README.md#Dynamic_programming-Trees-DP_over_children)
* [Graph theory](/README.md#Graph_theory) > [Depth first search](/README.md#Graph_theory-Depth_first_search)
