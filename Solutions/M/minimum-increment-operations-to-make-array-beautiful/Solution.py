# https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        dp = [[0, 0, 0] for _ in nums]
        for i, x in enumerate(nums):
            add = max(0, k-x)
            dp[i][0] = add + (min([y for y in dp[i-1]]) if i else 0)
            for j in range(1, min(3, i+1)):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j-1])
        return min([y for y in dp[-1]])
