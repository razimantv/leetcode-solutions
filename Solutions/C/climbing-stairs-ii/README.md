# Climbing stairs ii

[Problem link](https://leetcode.com/problems/climbing-stairs-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/climbing-stairs-ii/


class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        @cache
        def dp(n):
            if n < 0:
                return inf
            elif n == 0:
                return 0
            else:
                return costs[n - 1] + min(
                    d**2 + dp(n - d) for d in range(1, 4)
                )

        return dp(len(costs))
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
