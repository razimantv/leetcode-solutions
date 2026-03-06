# Check if binary string has at most one segment of ones

[Problem link](https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return sum(1 for x, y in pairwise('0' + s) if x + y == '01') < 2
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
