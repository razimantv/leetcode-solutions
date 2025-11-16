# Number of substrings with only 1s

[Problem link](https://leetcode.com/problems/number-of-substrings-with-only-1s/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution:
    def numSub(self, s: str) -> int:
        cur, ret = 0, 0
        for c in s:
            if c == '1':
                cur += 1
                ret += cur
            else:
                cur = 0
        return ret % (10 ** 9 + 7)
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
