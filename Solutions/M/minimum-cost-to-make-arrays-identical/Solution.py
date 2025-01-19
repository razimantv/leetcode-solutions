# https://leetcode.com/problems/minimum-cost-to-make-arrays-identical

class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        c1 = sum(abs(y - x) for x, y in zip(arr, brr))
        c2 = k + sum(abs(y - x) for x, y in zip(sorted(arr), sorted(brr)))
        return min(c1, c2)
