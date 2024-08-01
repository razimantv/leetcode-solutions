# Calculate money in leetcode bank

[Problem link](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        return sum(
            (
                2 * i + 1 + 
                (days := (n//7 + (1 if i < n % 7 else 0)))
            ) * days // 2
            for i in range(7)
        )
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
