# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

import numpy as np


class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        i1, i2 = sorted([np.argmin(nums), np.argmax(nums)])
        return int(min(i2 + 1, n - i1, i1 + 1 + n - i2))
