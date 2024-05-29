# https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, k: int) -> int:
        diff = [abs(ord(c) - ord(d)) for c, d in zip(s, t)]
        l, ret = 0, 0
        for r, x in enumerate(diff):
            k -= x
            while k < 0:
                k += diff[l]
                l += 1
            ret = max(ret, r - l + 1)
        return ret
