# Count the number of arrays with k matching adjacent elements

[Problem link](https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements

mod = 10 ** 9 + 7


def modpow(a, n):
    ret = 1
    while n:
        if n & 1:
            ret = (ret * a) % mod
        a = (a * a) % mod
        n >>= 1
    return ret


def choose(n, r):
    if 2 * r > n:
        r = n - r
    num, den = 1, 1
    for i in range(r):
        num, den = (num * (n - i)) % mod, (den * (r - i)) % mod
    return (num * modpow(den, mod - 2)) % mod


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return (m * modpow(m - 1, n - k - 1) * choose(n - 1, k)) % mod
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Modular exponentiation/inverse](/Collections/mathematics.md#modular-exponentiation-inverse)
