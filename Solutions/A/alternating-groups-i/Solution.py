# https://leetcode.com/problems/alternating-groups-i/

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        k = 3
        colors += colors[:k-1]
        cur, ret = 1, 0
        for x, y in pairwise(colors):
            if x == y:
                cur = 1
            else:
                cur += 1
            if cur >= k:
                ret += 1
        return ret
