# https://leetcode.com/problems/count-the-hidden-sequences/

class Solution:
    def numberOfArrays(
        self, differences: list[int], lower: int, upper: int
    ) -> int:
        ar = [0] + list(accumulate(differences))
        return max(0, upper - lower - (max(ar) - min(ar)) + 1)
