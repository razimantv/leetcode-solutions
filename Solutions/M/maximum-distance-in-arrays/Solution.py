# https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        small = sorted([(a[0], i) for i, a in enumerate(arrays)])[:2]
        big = sorted([(a[-1], i) for i, a in enumerate(arrays)])[-2:]
        return max(y-x for y, i in big for x, j in small if i != j)
