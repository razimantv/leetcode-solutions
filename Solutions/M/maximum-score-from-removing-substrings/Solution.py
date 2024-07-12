# https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            c1, c2 = 'a', 'b'
        else:
            c1, c2 = 'b', 'a'
            x, y = y, x
        n1, n2, ret = 0, 0, 0
        for c in s:
            if c == c2:
                if n1:
                    n1 -= 1
                    ret += x
                else:
                    n2 += 1
            elif c == c1:
                n1 += 1
            else:
                ret += min(n1, n2) * y
                n1, n2 = 0, 0
        return ret + min(n1, n2) * y
