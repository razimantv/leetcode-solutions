# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        def proc(nums):
            tot, cnt = 0, 0
            for x in nums:
                tot += x
                if not x:
                    tot += 1
                    cnt += 1
            return tot, cnt

        tot1, cnt1 = proc(nums1)
        tot2, cnt2 = proc(nums2)

        if tot1 == tot2:
            return tot1
        elif tot1 > tot2:
            return tot1 if cnt2 else -1
        else:
            return tot2 if cnt1 else -1
