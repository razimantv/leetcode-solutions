# Maximum prime difference

[Problem link](https://leetcode.com/problems/maximum-prime-difference/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-prime-difference/

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isprime(x):
            if x == 1:
                return False
            for i in range(2, x):
                if i * i > x:
                    return True
                if x % i == 0:
                    return False
            return True

        good = [i for i, x in enumerate(nums) if isprime(x)]
        return good[-1] - good[0]
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
