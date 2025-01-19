# Manhattan distances of all arrangements of pieces

[Problem link](https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces

class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        def modpow(a, n, mod):
            ret = 1
            while n:
                if n & 1:
                    ret = (ret * a) % mod
                a, n = (a * a) % mod, n >> 1
            return ret

        def invmod(x, mod):
            return modpow(x, mod - 2, mod)

        def choose(n, r, mod):
            r, num, den = min(r, n - r), 1, 1
            for i in range(1, r + 1):
                num, den = (num * (n - i + 1)) % mod, (den * i) % mod
            return (num * invmod(den, mod)) % mod

        mod = 10 ** 9 + 7
        rest = choose(m * n - 2, k - 2, mod)
        return (
            m * n * (m * (n ** 2 - 1) + n * (m ** 2 - 1)) * rest // 6
        ) % mod
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Modular exponentiation/inverse](/Collections/mathematics.md#modular-exponentiation-inverse)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
