# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n):
            digs = list(map(int, str(n)))
            return sum((
                1 for i in range(2, len(digs)) 
                if (digs[i] - digs[i -1]) * (digs[i - 1] - digs[i - 2]) < 0
            ))
        return sum(waviness(n) for n in range(num1, num2 + 1))
