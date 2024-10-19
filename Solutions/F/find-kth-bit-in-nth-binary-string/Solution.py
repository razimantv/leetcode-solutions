# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        flip, msb = 0, 1 << 20
        while k > 1 and msb:
            if msb & k:
                k = msb - (msb ^ k)
                flip ^= 1
            msb >>= 1
        return str(flip)
