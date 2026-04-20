# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        for i, x in enumerate(colors):
            if x != colors[-1]:
                ret = n - 1 - i
                break
        for i, x in enumerate(colors[::-1]):
            if x != colors[0]:
                ret = max(ret, n - 1 - i)
                break
        return ret
