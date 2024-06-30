# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        for x in nums:
            y = x % k
            todo = [0] * k
            for yp in range(k):
                z = (y + yp) % k
                todo[yp] = max(dp[z][y], dp[z][yp] + 1)
            for yp in range(k):
                z = (y + yp) % k
                dp[z][y] = todo[yp]
        return max(max(row) for row in dp)
