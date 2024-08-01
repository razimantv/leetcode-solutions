# Minimum number of changes to make binary string beautiful

[Problem link](https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

class Solution:
    def minChanges(self, s: str) -> int:
        ret = 0
        for i in range(1, len(s), 2):
            if s[i] != s[i-1]:
                ret += 1
        return ret
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
