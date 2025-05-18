# Painting a grid with three different colors

[Problem link](https://leetcode.com/problems/painting-a-grid-with-three-different-colors/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        poss, mod = [[0], [1], [2]], 10 ** 9 + 7
        for L in range(m - 1):
            poss = [
                old + [i] for old in poss for i in range(3) if i != old[-1]
            ]

        neigh = [
            [
                i for i, P2 in enumerate(poss)
                if all(x != y for x, y in zip(P1, P2))
            ]
            for P1 in poss
        ]

        dp = [1 for P in poss]
        for L in range(n - 1):
            dp = [sum(dp[j] for j in neigh[i]) % mod for i, x in enumerate(dp)]
        return sum(dp) % mod
```
## Tags

* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Elementwise processing using a vector](/Collections/brute-force-enumeration.md#elementwise-processing-using-a-vector)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Graph-like state transitions](/Collections/dynamic-programming.md#graph-like-state-transitions)
