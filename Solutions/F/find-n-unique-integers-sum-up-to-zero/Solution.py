# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> list[int]:
        return list(range(1, n)) + [-(n - 1) * n // 2]
