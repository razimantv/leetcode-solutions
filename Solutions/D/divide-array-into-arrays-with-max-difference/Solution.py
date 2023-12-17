# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        if n % 3:
            return []
        nums = sorted(nums)
        ret = []
        for l in range(0, n, 3):
            if nums[l+2] - nums[l] > k:
                return []
            ret.append(nums[l:l+3])
        return ret
