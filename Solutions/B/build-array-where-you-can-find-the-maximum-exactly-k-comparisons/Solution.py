# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

class Solution:
    @cache
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0:
            return 0 if n else 1
        if n < k or m < k:
            return 0
        ret = self.numOfArrays(n, m-1, k)
        for pos in range(k, n+1):
            ret = (
                ret + self.numOfArrays(pos-1, m-1, k-1) * (m ** (n-pos))
            ) % 1000000007
        return ret
