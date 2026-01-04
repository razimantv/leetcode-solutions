# Four divisors

[Problem link](https://leetcode.com/problems/four-divisors/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/four-divisors/

class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        squares = set(i * i for i in range(1, 317))
        ret = 0
        for x in nums:
            if x in squares:
                continue
            fac = 0
            for y in range(2, int(sqrt(x)) + 1):
                if not x % y:
                    if fac:
                        break
                    fac = y
            else:
                if fac:
                    ret += 1 + fac + x + x // fac
        return ret
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Factor listing in sqrt(N)](/Collections/mathematics.md#factor-listing-in-sqrt-n-)
