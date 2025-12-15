# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        ret, cur = 1, 1
        for x, y in pairwise(prices):
            cur = cur + 1 if x - y == 1 else 1
            ret += cur
        return ret
