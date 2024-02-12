# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, best = 0, 0
        for x in nums:
            if cnt == 0:
                cnt, best = 1, x
            else:
                cnt += 1 if x == best else -1
        return best
