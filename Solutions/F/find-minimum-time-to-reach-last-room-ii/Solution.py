# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

from sortedcontainers import SortedList


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        mindist = {(0, 0): 0}
        todo = SortedList([(0, 0, 0)])
        while len(todo):
            d, i, j = todo.pop(0)
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ii, jj = i + di, j + dj
                if not (0 <= ii < m and 0 <= jj < n):
                    continue
                dd = max(d, moveTime[ii][jj]) + 1 + ((i + j) & 1)
                if (ii, jj) not in mindist or mindist[(ii, jj)] > dd:
                    if (ii, jj) in mindist:
                        todo.remove((mindist[(ii, jj)], ii, jj))
                    mindist[(ii, jj)] = dd
                    todo.add((dd, ii, jj))
        return mindist[(m - 1, n - 1)]
