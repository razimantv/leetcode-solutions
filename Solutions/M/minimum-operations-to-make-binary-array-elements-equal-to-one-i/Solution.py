# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, ret = len(nums), 0
        for i in range(n - 2):
            if not nums[i]:
                ret += 1
                nums[i:i+3] = [1 - x for x in nums[i:i+3]]
        return ret if nums[-1] == nums[-2] == 1 else -1
