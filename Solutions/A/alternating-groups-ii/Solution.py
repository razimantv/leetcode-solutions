# https://leetcode.com/problems/alternating-groups-ii/

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
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
