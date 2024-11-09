# https://leetcode.com/problems/smallest-divisible-digit-product-i/

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digprod(n):
            ret = 1
            for d in str(n):
                ret *= int(d)
            return ret

        while digprod(n) % t:
            n += 1
        return n
