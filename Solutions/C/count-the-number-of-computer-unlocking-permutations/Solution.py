# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        if complexity[0] >= min(complexity[1:]):
            return 0

        ret = 1
        for i in range(1, len(complexity)):
            ret = (ret * i) % (10 ** 9 + 7)
        return ret
