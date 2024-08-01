# Harshad number

[Problem link](https://leetcode.com/problems/harshad-number/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/harshad-number/

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        dsum = sum(int(d) for d in str(x))
        return dsum if x % dsum == 0 else -1
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
