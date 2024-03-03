# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return len([x for x in nums if x < k])
