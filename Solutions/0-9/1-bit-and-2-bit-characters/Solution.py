# https://leetcode.com/problems/1-bit-and-2-bit-characters/

class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n, i = len(bits), 0

        while i < n:
            if i == n - 1:
                return True
            i += bits[i] + 1
        return False
