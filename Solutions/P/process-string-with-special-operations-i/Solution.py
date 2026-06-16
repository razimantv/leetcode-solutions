# https://leetcode.com/problems/process-string-with-special-operations-i/

class Solution:
    def processStr(self, s: str) -> str:
        ret = []
        for c in s:
            if c == '*':
                if ret:
                    ret.pop()
            elif c == '#':
                ret += ret
            elif c == '%':
                ret = ret[::-1]
            else:
                ret. append (c)
        return ''. join(ret)
