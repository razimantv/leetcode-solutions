# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n, ret = len(nums), 0
        pref = [0] * (n + 1)

        for i, x in enumerate(nums):
            pref[i] ^= pref[i - 1] if i else 0
            if not x ^ pref[i]:
                if i + k > n:
                    return -1
                pref[i] ^= 1
                pref[i + k] ^= 1
                ret += 1
        return ret
