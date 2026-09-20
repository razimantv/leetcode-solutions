# Reverse degree of a string

[Problem link](https://leetcode.com/problems/reverse-degree-of-a-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/reverse-degree-of-a-string/

class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((ord('z') + 1 - ord(c)) * (i + 1) for i, c in enumerate(s))
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
