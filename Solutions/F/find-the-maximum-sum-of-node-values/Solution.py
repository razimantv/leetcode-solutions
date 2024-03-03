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
