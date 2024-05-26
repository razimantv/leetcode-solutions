# https://leetcode.com/problems/special-array-i/

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all((x + y) & 1 for x, y in pairwise(nums))
