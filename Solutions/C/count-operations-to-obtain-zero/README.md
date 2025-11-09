# Count operations to obtain zero

[Problem link](https://leetcode.com/problems/count-operations-to-obtain-zero/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-operations-to-obtain-zero/

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ret = 0
        if num1 > num2:
            num1, num2 = num2, num1

        while num1:
            ret += num2 // num1
            num1, num2 = num2 % num1, num1
        return ret
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [GCD/LCM](/Collections/mathematics.md#gcd-lcm)
