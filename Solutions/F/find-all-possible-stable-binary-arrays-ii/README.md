# Find all possible stable binary arrays ii

[Problem link](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, lim: int) -> int:
        mod = 10 ** 9 + 7

        def add(a, b):
            return (a + b) % mod

        def sub(a, b):
            return add(a, mod - b % mod)

        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp0[0][0], dp1[0][0], dp0[1][0], dp1[0][1] = 1, 1, 1, 1
        for i in range(zero + 1):
            for j in range(one + 1):
                if i + j < 2:
                    continue
                if i:
                    dp0[i][j] = add(dp0[i][j], dp0[i - 1][j] + dp1[i - 1][j])
                if j:
                    dp1[i][j] = add(dp1[i][j], dp0[i][j - 1] + dp1[i][j - 1])
                if i > lim:
                    dp0[i][j] = sub(dp0[i][j], dp1[i - lim - 1][j])
                if j > lim:
                    dp1[i][j] = sub(dp1[i][j], dp0[i][j - lim - 1])
        return add(dp0[-1][-1], dp1[-1][-1])
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics) > [Inclusion-exclusion](/Collections/mathematics.md#inclusion-exclusion)
