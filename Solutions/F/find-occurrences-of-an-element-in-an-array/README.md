# Find occurrences of an element in an array

[Problem link](https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        pos = [i for i, y in enumerate(nums) if x == y]
        return [pos[p - 1] if p <= len(pos) else -1 for p in queries]
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
