# Find the number of possible ways for an event

[Problem link](https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        # sum_{g} ways(n, g) y^g
        # ways(n, g) = g ways(g) + (x - g + 1) ways(g - 1)

        mod = 10 ** 9 + 7
        ways = [1] + [0] * x
        for i in range(n):
            for g in range(x, 0, -1):
                ways[g] = (g * ways[g] + (x - g + 1) * ways[g - 1]) % mod
            ways[0] = 0

        ret, ypow = 0, 1
        for i in range(1, x + 1):
            ypow = (ypow * y) % mod
            ret = (ret + ypow * ways[i]) % mod
        return ret
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
