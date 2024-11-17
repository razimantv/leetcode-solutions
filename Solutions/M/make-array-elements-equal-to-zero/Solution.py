# https://leetcode.com/problems/make-array-elements-equal-to-zero

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        tot, ret = sum(nums), 0
        for x, y in pairwise([0] + list(accumulate(nums))):
            if x == y and abs(2 * x - tot) < 2:
                ret += 2 - (tot & 1)
        return ret
