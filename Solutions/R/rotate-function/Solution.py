# https://leetcode.com/problems/rotate-function/

class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        cur, tot = sum((i * x for i, x in enumerate(nums))), sum(nums)
        ret, n = cur, len(nums)
        for x in nums:
            cur += n * x - tot
            ret = max(ret, cur)
        return ret
