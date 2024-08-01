# Make three strings equal

[Problem link](https://leetcode.com/problems/make-three-strings-equal/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/make-three-strings-equal/

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        good = 0
        l1, l2, l3 = len(s1), len(s2), len(s3)
        for i in range(min(l1, l2, l3)):
            if s1[i] == s2[i] == s3[i]:
                good = i + 1
            else:
                break
        if not good:
            return -1
        return l1 + l2 + l3 - 3 * good
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
