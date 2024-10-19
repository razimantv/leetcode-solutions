# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1:
            return "0"
        a, b = 1, 3
        while k > b:
            a, b = b, 2 * b + 1
        flip = 0
        while True:
            if k == 1:
                break
            elif k == a + 1:
                return str(1 ^ flip)
            if k > a + 1:
                k = b - k + 1
                flip ^= 1
            a, b = a // 2, a
        return str(flip)
