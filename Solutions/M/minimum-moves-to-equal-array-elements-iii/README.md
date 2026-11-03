# Minimum moves to equal array elements iii

[Problem link](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m = max(nums)
        return sum(m - x for x in nums)
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
