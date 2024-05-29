# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution:
    def numSteps(self, s: str) -> int:
        ret, end, ones = 0, True, 0
        for c in s[::-1]:
            if c == '0':
                ret += 1 if end else 2
            else:
                ret += 2 if end else 1
                ones += 1
                end = False
        if ones == 1:
            ret -= 2
        return ret
