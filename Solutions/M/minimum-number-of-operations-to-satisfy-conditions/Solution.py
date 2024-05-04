# https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * 10
        for j in range(n):
            ctr = Counter(grid[i][j] for i in range(m))
            newdp = []
            for i in range(10):
                newdp. append(
                    m - ctr[i] + min(dp[ii] for ii in range(10) if ii != i)
                )
            dp = newdp
        return min(dp)
