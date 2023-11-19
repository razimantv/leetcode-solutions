# https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        ret, white = 0, 0
        for c in s:
            if c == '0':
                ret += white
            else:
                white += 1
        return ret
