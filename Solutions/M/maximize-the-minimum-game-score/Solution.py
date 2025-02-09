# https://leetcode.com/problems/maximize-the-minimum-game-score/

class Solution:
    def maxScore(self, points: list[int], m: int) -> int:
        n = len(points)

        def work(val):
            ret, free, skip = 0, 0, 0
            for x in points:
                cur = (val + x - 1) // x
                if free >= cur:
                    free, skip = 0, skip + 1
                else:
                    ret += 2 * (cur - free) + skip - 1
                    free = max(cur - free - 1, 0)
                    skip = 0
            return ret <= m

        if m < n:
            return 0

        start, end = 0, min(points) * m + 1
        while end - start > 1:
            mid = (end + start) // 2
            if work(mid):
                start = mid
            else:
                end = mid
        return start
