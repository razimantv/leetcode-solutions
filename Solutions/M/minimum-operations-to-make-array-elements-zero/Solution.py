# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

def dp(n):
    if n == 0:
        return 0
    start, end, ret, cur = 1, 4, 0, 1
    while start <= n:
        ret += cur * (min(n, end - 1) - start + 1)
        start, end, cur = end, end << 2, cur + 1
    return ret


class Solution:
    def minOperations(self, queries: list[list[int]]) -> int:
        return sum((dp(r) - dp(l - 1) + 1) >> 1 for l, r in queries)
