# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii

class Solution:
    def maxFreeTime(
        self, event: int, start: list[int], end: list[int]
    ) -> int:
        n, durations = len(start), [e - s for s, e in zip(start, end)]
        start.append(event)
        end = [0] + end
        gaps = [s - e for s, e in zip(start, end)]
        ret = max(gaps)
        left = list(accumulate(gaps, max))
        right = list(accumulate(gaps[::-1], max))[::-1]
        for i, d in enumerate(durations):
            ret = max(ret, gaps[i] + gaps[i + 1])
            if (i and left[i - 1] >= d) or (i < n - 1 and right[i + 2] >= d):
                ret = max(ret, gaps[i] + gaps[i + 1] + d)
        return ret
