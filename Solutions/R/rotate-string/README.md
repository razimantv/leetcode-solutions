# Rotate string

[Problem link](https://leetcode.com/problems/rotate-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(goal) == len(s) and goal in s+s
```
## Tags

* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Cylic array](/Collections/string.md#cylic-array)
