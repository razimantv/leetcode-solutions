# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def conv(x):
            if x == 2:
                return -1
            for i in range(31):
                if (x & (1 << i)) and not (x & (1 << (i + 1))):
                    return x ^ (1 << i)

        return [conv(x) for x in nums]
