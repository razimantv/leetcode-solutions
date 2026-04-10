# Minimum distance between three equal elements i

[Problem link](https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        last, ret = defaultdict(list), inf
        for i, x in enumerate(nums):
            if len(last[x]) == 2:
                ret = min(ret, 2 * (i - last[x][1]))
            last[x] = ([i] + last[x])[:2]
        return -1 if ret == inf else ret
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with same value](/Collections/array-scanning.md#location-of-previous-element-with-same-value)
