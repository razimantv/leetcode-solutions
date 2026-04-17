# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        ret, last = inf, {}
        for i, x in enumerate(nums[::-1]):
            y = int(str(x)[::-1])
            if y in last:
                ret = min(ret, i - last[y])
            last[x] = i
        return -1 if ret == inf else ret
