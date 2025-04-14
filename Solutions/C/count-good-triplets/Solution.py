# https://leetcode.com/problems/count-good-triplets/

class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        return sum(
            1 for ai, aj, ak in combinations(arr, 3)
            if abs(ai - aj) <= a and abs(aj - ak) <= b and abs(ai - ak) <= c
        )
