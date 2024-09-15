# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [x for x, y in Counter(nums).items() if y > 1]
