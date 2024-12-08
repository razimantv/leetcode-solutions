# https://leetcode.com/problems/transformed-array/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[(i + n + nums[i] % n) % n] for i in range(n)]
