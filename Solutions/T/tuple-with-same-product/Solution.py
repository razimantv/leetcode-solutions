# https://leetcode.com/problems/tuple-with-same-product/

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        ctr = Counter(
            nums[i] * nums[j]
            for i in range(len(nums)) for j in range(i)
        )
        return sum(x * (x - 1) * 4 for x in ctr. values())
