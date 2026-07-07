# Concatenate non zero digits and multiply by sum i

[Problem link](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if not n:
            return 0
        digs = list(str(n))
        return int(''. join(c for c in digs if c != '0')) * sum(map(int, digs))
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
