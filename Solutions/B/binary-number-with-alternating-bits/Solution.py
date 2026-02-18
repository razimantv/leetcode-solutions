# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n & 1:
            n >>= 1
        while n:
            if (n & 3) != 2:
                return False
            n >>= 2
        return True
