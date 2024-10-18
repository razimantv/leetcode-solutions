# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        xor, cnt = 0, 0
        for mask in range(1 << len(nums)):
            cur = 0
            for i, x in enumerate(nums):
                if mask & (1 << i):
                    cur |= x
            if cur > xor:
                xor, cnt = cur, 1
            elif cur == xor:
                cnt += 1
        return cnt
