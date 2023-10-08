# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        tot = 0
        for i in range(1, n+1):
            tot += i if i % m == 0 else -i
        return -tot
