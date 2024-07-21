# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

class Solution:
    def maxOperations(self, s: str) -> int:
        ret, g = 0, 0
        for x, y in pairwise(s[::-1]):
            if x == '0' and y == '1':
                g += 1
            if y == '1':
                ret += g
        return ret
