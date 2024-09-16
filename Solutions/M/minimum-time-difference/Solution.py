# https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, time: List[str]) -> int:
        time = sorted(list(map(lambda x: int(x[:2]) * 60 + int(x[3:]), time)))
        return min(y-x for x, y in pairwise(time + [time[0] + 1440]))
