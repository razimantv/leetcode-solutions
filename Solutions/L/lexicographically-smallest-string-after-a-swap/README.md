# Lexicographically smallest string after a swap

[Problem link](https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

class Solution:
    def getSmallestString(self, s: str) -> str:
        n = len(s)
        for i in range(1, n):
            x, y = s[i-1:i+1]
            if y < x and int(x) % 2 == int(y) % 2:
                return s[:i-1] + y + x + s[i+1:]
        return s
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
