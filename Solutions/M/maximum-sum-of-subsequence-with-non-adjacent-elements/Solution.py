# https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

class Solution:
    def maximumSumSubsequence(
        self, nums: List[int], queries: List[List[int]]
    ) -> int:
        n, base = len(nums), 1
        while base < n:
            base <<= 1

        seg = [[[0, 0], [0, 0]] for _ in range(2 * base)]

        def merge(node):
            lc, rc = node * 2, node * 2 + 1
            for l in [0, 1]:
                for r in [0, 1]:
                    seg[node][l][r] = max(
                        seg[lc][l][lcr] + seg[rc][rcl][r]
                        for lcr, rcl in [[0, 0], [0, 1], [1, 0]]
                    )

        for i, x in enumerate(nums):
            seg[base + i] = [[0, 0], [0, x]]
        for i in range(base - 1, 0, -1):
            merge(i)

        ret = 0
        for i, x in queries:
            node = base + i
            seg[node][1][1] = x
            node >>= 1
            while node:
                merge(node)
                node >>= 1
            ret += max(seg[1][0] + seg[1][1])
        return ret % (10 ** 9 + 7)
