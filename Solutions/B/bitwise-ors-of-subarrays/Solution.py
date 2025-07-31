# https://leetcode.com/problems/bitwise-ors-of-subarrays/

class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        last, ors = [-1] * 31, set()
        for i, x in enumerate(arr):
            for b in range(30):
                if x & (1 << b):
                    last[b] = i
            y = 0
            ors.add(x)
            for p, q in pairwise(sorted(last, reverse=True)):
                if p != q:
                    y |= arr[p]
                    ors.add(y)
        return len(ors)
