# https://leetcode.com/problems/score-of-a-string/

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(c)-ord(d)) for c, d in pairwise(s))
