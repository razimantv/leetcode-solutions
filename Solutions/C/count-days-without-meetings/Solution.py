# https://leetcode.com/problems/count-days-without-meetings/

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        endpoints = sorted(
            [
                (meeting[i] + i, 1 - 2 * i)
                for meeting in meetings for i in [0, 1]
            ] + [(days + 1, 1)]
        )
        prev, cur, ret = 1, 0, 0
        for day, endtype in endpoints:
            if cur == 0:
                ret += day - prev
            prev = day
            cur += endtype
        return ret
