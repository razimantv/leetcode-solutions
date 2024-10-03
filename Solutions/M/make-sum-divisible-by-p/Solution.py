# https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n, rem = len(nums), sum(nums) % p
        if not rem:
            return 0
        last, pref, ret = {0: -1}, 0, n
        for i, x in enumerate(nums):
            pref = (pref + x) % p
            target = (pref + p - rem) % p
            if target in last:
                ret = min(ret, i - last[target])
            last[pref] = i
        return -1 if ret == n else ret
