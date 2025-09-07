# Find n unique integers sum up to zero

[Problem link](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> list[int]:
        return list(range(1, n)) + [-(n - 1) * n // 2]
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
