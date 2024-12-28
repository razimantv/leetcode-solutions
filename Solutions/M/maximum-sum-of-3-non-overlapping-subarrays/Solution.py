# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n, psum = len(nums), [0] + list(accumulate(nums))
        dp = [[0] + [-math.inf] * 3 for _ in range(n + 1)]
        for i in range(k, n + 1):
            cur = psum[i] - psum[i - k]
            for j in range(1, 4):
                dp[i][j] = max(dp[i - 1][j], dp[i - k][j - 1] + cur)

        ret, i, j = [], n, 3
        while j:
            if dp[i][j] == dp[i - 1][j]:
                i -= 1
            else:
                ret.append(i := i - k)
                j -= 1
        return ret[::-1]
