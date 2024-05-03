# https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        mono, ret = [], 0
        for i, x in enumerate(nums):
            while mono and mono[-1][0] < x:
                mono.pop()
            if mono and mono[-1][0] == x:
                mono[-1][1] += 1
            else:
                mono.append([x, 1])
            ret += mono[-1][1]
        return ret
