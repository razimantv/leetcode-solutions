# https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums1, nums2 = set(nums1), set(nums2)
        intersection = nums1.intersection(nums2)
        n1, n2, n12 = len(nums1), len(nums2), len(intersection)
        m1, m2 = min(n1 - n12, n // 2), min(n2 - n12, n // 2)
        return m1 + m2 + min(n - m1 - m2, n12)
