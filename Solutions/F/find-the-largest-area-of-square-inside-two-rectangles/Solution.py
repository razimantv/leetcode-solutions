# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        n, ret = len(bottomLeft), 0
        for i in range(n):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]
            for j in range(i):
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]
                xmin, xmax = max(x1, x3), min(x2, x4)
                ymin, ymax = max(y1, y3), min(y2, y4)
                ret = max(ret, min(xmax - xmin, ymax - ymin))
        return ret ** 2
