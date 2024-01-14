# https://leetcode.com/problems/count-elements-with-maximum-frequency/

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        mx = max(ctr.values())
        return sum(x for x in ctr.values() if x == mx)
