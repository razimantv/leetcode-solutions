# Minimum operations to make array equal to target

[Problem link](https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        diff = [x - y for x, y in zip(nums, target)]
        cur, ret = 0, 0
        for x in diff:
            if cur * x <= 0:
                cur = 0
            if abs(x) > abs(cur):
                ret += abs(x) - abs(cur)
            cur = x
        return ret
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
