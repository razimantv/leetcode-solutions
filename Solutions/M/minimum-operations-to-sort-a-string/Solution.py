# https://leetcode.com/problems/minimum-operations-to-sort-a-string/


class Solution:
    def minOperations(self, s: str) -> int:
        sl = list(s)
        if all(x <= y for x, y in pairwise(sl)):
            return 0
        elif len(sl) == 2:
            return -1
        a, b = min(sl), max(sl)
        if a == sl[0] or b == sl[-1]:
            return 1
        elif a in sl[:-1] or b in sl[1:]:
            return 2
        else:
            return 3
