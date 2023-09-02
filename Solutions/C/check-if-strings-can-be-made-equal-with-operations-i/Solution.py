# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1a = sorted(s1[::2])
        s1b = sorted(s1[1::2])
        s2a = sorted(s2[::2])
        s2b = sorted(s2[1::2])
        return s1a == s2a and s1b == s2b
