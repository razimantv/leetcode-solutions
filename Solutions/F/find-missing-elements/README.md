# Find missing elements

[Problem link](https://leetcode.com/problems/find-missing-elements/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-missing-elements/

class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        return sum(
            (list(range(x + 1, y)) for x, y in pairwise(sorted(nums))),
            start=[]
        )
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
