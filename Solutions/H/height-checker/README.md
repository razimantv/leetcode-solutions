# Height checker

[Problem link](https://leetcode.com/problems/height-checker/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len([1 for h, j in zip(heights, sorted(heights)) if h != j])
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
