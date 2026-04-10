# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        last, ret = defaultdict(list), inf
        for i, x in enumerate(nums):
            if len(last[x]) == 2:
                ret = min(ret, 2 * (i - last[x][1]))
            last[x] = ([i] + last[x])[:2]
        return -1 if ret == inf else ret
