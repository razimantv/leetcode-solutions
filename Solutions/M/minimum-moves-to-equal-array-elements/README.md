# Minimum moves to equal array elements

[Problem link](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m = min(nums)
        return sum(x - m for x in nums)
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
