# 2 keys keyboard

[Problem link](https://leetcode.com/problems/2-keys-keyboard/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/2-keys-keyboard/

class Solution:
    @cache
    def f(self, n):
        if n == 1:
            return 0
        ret = n
        i = 2
        while i * i <= n:
            if n % i == 0:
                ret = min(ret, self.f(n // i) + i, self.f(i) + n // i)
            i += 1
        return ret

    def minSteps(self, n: int) -> int:
        return self.f(n)
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Number theory](/Collections/dynamic-programming.md#number-theory)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Dynamic programming](/Collections/mathematics.md#dynamic-programming)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Factor listing in sqrt(N)](/Collections/mathematics.md#factor-listing-in-sqrt-n-)
