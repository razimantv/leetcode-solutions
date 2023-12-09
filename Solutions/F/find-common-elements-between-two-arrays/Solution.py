# https://leetcode.com/problems/find-common-elements-between-two-arrays/

class Solution:
    def findIntersectionValues(
        self, nums1: List[int], nums2: List[int]
    ) -> List[int]:
        return [
            len([x for x in nums1 if x in nums2]),
            len([x for x in nums2 if x in nums1])
        ]
