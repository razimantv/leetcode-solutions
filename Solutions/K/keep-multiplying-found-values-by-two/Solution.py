# https://leetcode.com/problems/keep-multiplying-found-values-by-two/

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        for x in sorted(nums):
            if x == original:
                original *= 2
        return original
