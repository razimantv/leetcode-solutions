# Maximum height of a triangle

[Problem link](https://leetcode.com/problems/maximum-height-of-a-triangle/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-height-of-a-triangle/

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def work(ar):
            L = 0
            while True:
                if ar[L & 1] > L:
                    ar[L & 1] -= L + 1
                    L += 1
                else:
                    break
            return L

        return max(work([red, blue]), work([blue, red]))
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
