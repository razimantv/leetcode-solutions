# https://leetcode.com/problems/minimum-positive-sum-subarray/

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        psum, n = [0] + list(accumulate(nums)), len(nums)
        ret = math.inf
        for L in range(l, r + 1):
            for i in range(n + 1 - L):
                cur = psum[i + L] - psum[i]
                if cur > 0:
                    ret = min(cur, ret)
        return ret if ret < 10 ** 9 else -1
