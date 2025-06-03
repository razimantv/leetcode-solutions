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
