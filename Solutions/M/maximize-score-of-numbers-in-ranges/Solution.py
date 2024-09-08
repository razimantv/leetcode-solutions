# https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start = sorted(start)

        def work(x):
            t = start[0]
            for s in start[1:]:
                t = max(t + x, s)
                if t > s + d:
                    return False
            return True

        b_start, b_end = 0, start[-1] + d + 1 - start[0]
        while b_end - b_start > 1:
            mid = (b_end + b_start) >> 1
            if work(mid):
                b_start = mid
            else:
                b_end = mid
        return b_start
