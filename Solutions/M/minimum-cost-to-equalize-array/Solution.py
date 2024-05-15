# https://leetcode.com/problems/minimum-cost-to-equalize-array/

class Solution:
    def minCostToEqualizeArray(
        self, nums: List[int], cost1: int, cost2: int
    ) -> int:
        a, b, n, s = min(nums), max(nums), len(nums), sum(nums)

        if n == 1:
            return 0
        elif n == 2:
            return (b - a) * cost1 % (10 ** 9 + 7)

        ops = b * n - s
        ret = cost1 * ops

        prev, end = 0, 0
        while end < 2:
            dmax = b - a
            rest = ops - dmax
            op2 = min(ops // 2, rest)
            ret = min(ret, (prev + op2) * cost2 + (ops - 2 * op2) * cost1)
            if dmax < n - 2:
                b += 1
                end += 1
                ops += n
                continue

            prev += op2
            b += 1
            a += op2
            ops += n - 2 * op2

        return ret % (10 ** 9 + 7)
