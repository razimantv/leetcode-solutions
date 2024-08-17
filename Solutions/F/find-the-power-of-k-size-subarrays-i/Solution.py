# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ret = []
        for i, x in enumerate(nums):
            if i and nums[i] == nums[i - 1] + 1:
                cur += 1
            else:
                cur = 1
            if i >= k - 1:
                ret.append(-1 if cur < k else x)
        return ret
