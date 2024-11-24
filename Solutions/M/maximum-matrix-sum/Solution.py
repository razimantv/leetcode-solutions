# https://leetcode.com/problems/maximum-matrix-sum/

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        tot, neg, maxn, minp = 0, 0, -math.inf, math.inf
        for row in matrix:
            for x in row:
                tot += abs(x)
                if x < 0:
                    neg += 1
                    maxn = max(x, maxn)
                else:
                    minp = min(x, minp)
        if neg % 2 == 0:
            return tot
        elif neg == len(matrix) ** 2 or maxn >= -minp:
            return tot + 2 * maxn
        else:
            return tot - 2 * minp
