# https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            tmax = arr[i]
            dp[i] = max(
                dp[j] + (j-i) * (tmax := max(tmax, arr[j-1]))
                for j in range(i+1, min(i+k+1, n+1))
            )
        return dp[0]
