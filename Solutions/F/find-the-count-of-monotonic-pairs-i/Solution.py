# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = list(range(1, nums[0] + 2))
        for x, y in pairwise(nums):
            newdp = [0] * (y + 1)
            for i in range(max(0, y - x), y + 1):
                newdp[i] = dp[min(i, x, i + x - y)]
            dp = [x % mod for x in accumulate(newdp)]
        return dp[-1]
