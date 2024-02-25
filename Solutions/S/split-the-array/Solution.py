# https://leetcode.com/problems/split-the-array/

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return max(Counter(nums).values()) <= 2
