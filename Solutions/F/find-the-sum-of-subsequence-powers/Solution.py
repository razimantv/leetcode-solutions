# https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

class Solution:
    def sumOfPowers(self, nums: List[int], K: int) -> int:
        nums, n = sorted(nums), len(nums)
        diffs = sorted(list(set(
            nums[i] - nums[j] for i in range(n) for j in range(i)
        )))
        mod, prev, ret = 10 ** 9 + 7, 0, 0
        for d in diffs[::-1]:
            dpsum = [i for i in range(n + 1)]
            ii = [min(i, bisect_right(nums, nums[i]-d)) for i in range(n)]
            for k in range(2, K+1):
                old = dpsum.copy()
                for i in range(n):
                    dpsum[i + 1] = (dpsum[i] + old[ii[i]]) % mod
            ret = (ret + (dpsum[-1] + mod - prev) * d) % mod
            prev = dpsum[-1]
        return ret
