# https://leetcode.com/problems/two-best-non-overlapping-events/

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events. sort(key=lambda x: x[1])
        end = [event[1] for event in events]
        n, ret = len(events), 0
        best = [0] * n
        for i, (s, e, c) in enumerate(events):
            best[i] = max(c, best[i - 1] if i else 0)
            idx = bisect_left(end, s)
            if idx:
                ret = max(ret, c + best[idx - 1])
        return max(ret, best[-1])
