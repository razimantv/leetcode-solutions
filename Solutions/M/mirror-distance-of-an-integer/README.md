# Mirror distance of an integer

[Problem link](https://leetcode.com/problems/mirror-distance-of-an-integer/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/mirror-distance-of-an-integer/

class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
