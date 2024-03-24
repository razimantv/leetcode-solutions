# https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

class Solution:
    def minOperations(self, k: int) -> int:
        return min(x - 1 + (k - 1) // x for x in range(1, k + 1))
