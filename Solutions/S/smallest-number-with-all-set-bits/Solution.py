# https://leetcode.com/problems/smallest-number-with-all-set-bits/

class Solution:
    def smallestNumber(self, n: int) -> int:
        ret = 0
        while ret < n:
            ret = 2 * ret + 1
        return ret
