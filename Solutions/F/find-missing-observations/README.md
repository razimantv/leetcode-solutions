# Find missing observations

[Problem link](https://leetcode.com/problems/find-missing-observations/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n) - sum(rolls)
        if not (n <= total <= 6 * n):
            return []
        return [total // n + 1] * (total % n) + [total // n] * (n - total % n)
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
