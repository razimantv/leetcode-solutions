# Minimum pair removal to sort array i

[Problem link](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        ret = 0
        while True:
            flag, pair, idx = True, inf, -1
            for i, (x, y) in enumerate(pairwise(nums)):
                if x + y < pair:
                    pair, idx = x + y, i
                if x > y:
                    flag = False
            if flag:
                break
            ret += 1
            nums = nums[:idx] + [pair] + nums[idx + 2:]
        return ret
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
