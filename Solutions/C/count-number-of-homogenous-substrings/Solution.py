# https://leetcode.com/problems/count-number-of-homogenous-substrings/

class Solution:
    def countHomogenous(self, s: str) -> int:
        ret, cur = 1, 1
        for i in range(1, len(s)):
            cur = (cur + 1) if s[i] == s[i-1] else 1
            ret += cur
        return ret % (10**9 + 7)
