# Maximize consecutive elements in an array after modification

[Problem link](https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums = sorted(nums)
        inc, noinc, best = 1, 1, 1
        for x, y in pairwise(nums):
            if y == x:
                inc = max(inc, noinc + 1)
            elif y == x + 1:
                inc, noinc = inc + 1, noinc + 1
            elif y == x + 2:
                inc, noinc = 1, inc + 1
            else:
                inc, noinc = 1, 1
            best = max([best, inc, noinc])

        return best
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
