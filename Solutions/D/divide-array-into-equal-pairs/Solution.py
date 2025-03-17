# https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        return all(x & 1 == 0 for x in Counter(nums). values())
