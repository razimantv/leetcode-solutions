# https://leetcode.com/problems/jump-game-ix/

class Solution:
    def maxValue(self, nums: list[int]) -> list[int]:
        n, pmax = len(nums), list(accumulate(nums, max))
        ret, smin = [0] * n, list(accumulate(nums[::-1], min))[::-1]
        ret[-1] = pmax[-1]
        for i in range(n - 1, 0, -1):
            if pmax[i - 1] <= smin[i]:
                ret[i - 1] = pmax[i - 1]
            else:
                ret[i - 1] = ret[i]
        return ret
