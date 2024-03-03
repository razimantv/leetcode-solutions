# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        nums1, nums2 = [nums[0]], [nums[1]]
        for x in nums[2:]:
            if nums1[-1] > nums2[-1]:
                nums1.append(x)
            else:
                nums2.append(x)
        return nums1 + nums2
