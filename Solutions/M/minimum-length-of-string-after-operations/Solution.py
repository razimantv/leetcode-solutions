# https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution:
    def minimumLength(self, s: str) -> int:
        ret = 0
        for x in Counter(s).values():
            while x >= 3:
                x -= 2
            ret += x
        return ret
