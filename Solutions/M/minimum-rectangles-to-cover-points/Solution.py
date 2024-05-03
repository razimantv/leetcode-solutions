# https://leetcode.com/problems/minimum-rectangles-to-cover-points/

class Solution:
    def minRectanglesToCoverPoints(
        self, points: List[List[int]], w: int
    ) -> int:
        xvals = sorted([point[0] for point in points])
        ret, l, n = 1, 0, len(xvals)
        for r in range(n):
            if xvals[r] - xvals[l] > w:
                ret += 1
                l = r
        return ret
