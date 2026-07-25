# https://leetcode.com/problems/maximum-product-of-two-digits

class Solution:
    def maxProduct(self, n: int) -> int:
        c, d = map(int, sorted(str(n))[-2:])
        return c * d
