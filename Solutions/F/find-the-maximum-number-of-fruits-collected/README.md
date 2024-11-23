# Find the maximum number of fruits collected

[Problem link](https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ret = sum(fruits[i][i] for i in range(n))

        dp = [fruits[0][n - 1]] + [-math.inf] * (n - 2)
        for r in range(1, n - 1):
            dp = [
                max(dp[max(0, i - 1):min(i + 2, len(dp))]) +
                fruits[r][n - 1 - i]
                for i in range(n - 1 - r)
            ]
        ret += dp[0]

        dp = [fruits[n - 1][0]] + [-math.inf] * (n - 2)
        for r in range(1, n - 1):
            dp = [
                max(dp[max(0, i - 1):min(i + 2, len(dp))]) +
                fruits[n - 1 - i][r]
                for i in range(n - 1 - r)
            ]
        ret += dp[0]

        return ret
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
