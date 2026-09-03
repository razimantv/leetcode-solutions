# https://leetcode.com/problems/construct-uniform-parity-array-ii/

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        cnt = Counter(x & 1 for x in nums1)
        return bool((len(cnt) == 1) or (min(nums1) & 1))
