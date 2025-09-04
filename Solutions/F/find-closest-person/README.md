# Find closest person

[Problem link](https://leetcode.com/problems/find-closest-person/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-closest-person/

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1, d2 = abs(x - z), abs(y - z)
        return 1 if d1 < d2 else 2 if d2 < d1 else 0
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
