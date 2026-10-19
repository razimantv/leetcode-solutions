# Find target indices after sorting array

[Problem link](https://leetcode.com/problems/find-target-indices-after-sorting-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        return [i for i, x in enumerate(sorted(nums)) if x == target]
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
