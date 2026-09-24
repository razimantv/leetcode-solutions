# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/


class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i, x in enumerate(nums):
            if sum(map(int, str(x))) == i:
                return i
        return -1
