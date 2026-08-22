# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        return n % sum(fn(map(int, str(n))) for fn in [sum, prod]) == 0
