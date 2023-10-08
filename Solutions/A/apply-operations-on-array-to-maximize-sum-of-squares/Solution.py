# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        bits = [[0]*N for i in range(30)]
        for i, x in enumerate(nums):
            for b in range(30):
                if x & (1 << b):
                    bits[b][i] = 1

        bits = [sorted(_)[::-1] for _ in bits]
        ret = 0
        for i in range(k):
            x = sum((1 << b)*bits[b][i] for b in range(30))
            ret += x**2
        return ret % 1000000007
