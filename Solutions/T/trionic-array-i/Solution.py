# https://leetcode.com/problems/trionic-array-i/

class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        cnt, prev = 0, -1
        for x, y in pairwise(nums):
            if x == y:
                return False
            elif (x > y) != prev:
                cnt, prev = cnt + 1, x > y
        return cnt == 3 and prev == 0
