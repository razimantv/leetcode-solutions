# https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def good(l, r):
            ar = sorted(nums[l:r+1])
            d, a = ar[1] - ar[0], ar[0]
            for x in ar[1:]:
                if x - a != d:
                    return False
                a = x
            return True

        return [good(i, j) for i, j in zip(l, r)]
