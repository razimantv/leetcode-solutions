# https://leetcode.com/problems/clear-digits/

class Solution:
    def clearDigits(self, s: str) -> str:
        ret = []
        for c in s:
            if c in '0123456789':
                ret.pop()
            else:
                ret.append(c)
        return ''.join(ret)
