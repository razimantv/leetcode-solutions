# Lexicographically smallest string after operations with constraint

[Problem link](https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ret = ''
        for i, c in enumerate(s):
            cc = ord(c) - ord('a')
            for x in range(cc + 1):
                cur = min(cc - x, 26 - cc + x)
                if cur <= k:
                    ret += chr(ord('a') + x)
                    k -= cur
                    break
        return ret
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
