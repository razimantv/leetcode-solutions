# Check divisibility by digit sum and product

[Problem link](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        return n % sum(fn(map(int, str(n))) for fn in [sum, prod]) == 0
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
