# https://leetcode.com/problems/substring-matching-pattern

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        l, r = p.split('*')
        if (pos := s.find(l)) == -1:
            return False
        return s.find(r, pos + len(l)) != -1
