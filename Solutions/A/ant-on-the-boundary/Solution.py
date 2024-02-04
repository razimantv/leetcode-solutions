# https://leetcode.com/problems/ant-on-the-boundary/

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        cur, ret = 0, 0
        for x in nums:
            cur += x
            if not cur:
                ret += 1
        return ret
