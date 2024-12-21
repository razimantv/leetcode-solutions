# Count paths with the given xor value

[Problem link](https://leetcode.com/problems/count-paths-with-the-given-xor-value)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-paths-with-the-given-xor-value

class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        m, n, mod = len(grid), len(grid[0]), 10 ** 9 + 7
        dp = [[[0] * 16 for _ in range(n)] for i in range(m)]
        dp[0][0][grid[0][0]] = 1
        for i in range(m):
            for j, x in enumerate(grid[i]):
                if i + j:
                    for y in range(16):
                        dp[i][j][y] = (
                            (dp[i - 1][j][y ^ x] if i else 0) + 
                            (dp[i][j - 1][y ^ x] if j else 0)
                        ) % mod

        return dp[-1][-1][k]
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Grid](/Collections/dynamic-programming.md#grid)
* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
