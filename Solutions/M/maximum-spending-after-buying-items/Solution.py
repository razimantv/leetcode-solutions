# https://leetcode.com/problems/maximum-spending-after-buying-items/

from sortedcontainers import SortedList


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m, n = len(values), len(values[0])
        pq = SortedList()
        for i, row in enumerate(values):
            pq.add((row[0], i, 0))

        mn, ret = m * n, 0
        for i in range(mn):
            val, row, pos = pq.pop()
            ret += val * (mn - i)
            if pos < n-1:
                pq.add((values[row][pos + 1], row, pos + 1))
        return ret
