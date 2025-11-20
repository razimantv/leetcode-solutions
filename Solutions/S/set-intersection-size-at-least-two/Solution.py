# https://leetcode.com/problems/set-intersection-size-at-least-two/

class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[1], -x[0]))
        n = len(intervals)
        marked, ret = [0] * n, 0
        for i, (x, y) in enumerate(intervals):
            while marked[i] < 2:
                ret += 1
                for j in range(i, n):
                    if intervals[j][0] <= y <= intervals[j][1]:
                        marked[j] += 1
                y -= 1
        return ret
