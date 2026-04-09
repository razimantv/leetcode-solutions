# Xor after range multiplication queries ii

[Problem link](https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        n, grouped, mod = len(nums), defaultdict(list), 10 ** 9 + 7
        for l, r, k, v in queries:
            grouped[(k, l % k)].append((l, r, v))

        for (k, s), q in grouped.items():
            ar = [1] * ((n + k - 1) // k)
            for l, r, v in q:
                a, b = (l - s) // k, (r - s) // k + 1
                ar[a] = (ar[a] * v) % mod
                if b < len(ar):
                    ar[b] = (ar[b] * pow(v, -1, mod)) % mod

            pmult = 1
            for x, i in zip(ar, range(s, n, k)):
                pmult = (pmult * x) % mod
                nums[i] = (nums[i] * pmult) % mod

        return reduce(operator.xor, nums)
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Modular exponentiation/inverse](/Collections/mathematics.md#modular-exponentiation-inverse)
* [Prefix](/Collections/prefix.md#prefix) > [Product](/Collections/prefix.md#product)
* [Range updates using prefix sum](/Collections/range-updates-using-prefix-sum.md#range-updates-using-prefix-sum)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Reduce problem dimension with proofs](/Collections/mathematics.md#reduce-problem-dimension-with-proofs)
