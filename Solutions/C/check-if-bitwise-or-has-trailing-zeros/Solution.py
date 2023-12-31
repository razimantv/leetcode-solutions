# https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        cnt = len([x for x in nums if x % 2 == 0])
        return cnt > 1
