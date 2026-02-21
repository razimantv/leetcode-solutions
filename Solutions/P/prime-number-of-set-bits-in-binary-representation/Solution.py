# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])
        return sum(
            1 for x in range(left, right + 1) if x.bit_count() in primes
        )
