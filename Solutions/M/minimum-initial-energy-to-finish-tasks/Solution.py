# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0])
        ret = 0
        for b, a in tasks:
            ret = max(ret + b, a)
        return ret
