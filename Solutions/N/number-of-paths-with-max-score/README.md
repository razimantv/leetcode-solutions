# Number of paths with max score

[Problem link](https://leetcode.com/problems/number-of-paths-with-max-score/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-paths-with-max-score/

class Solution:
    def pathsWithMaxScore(self, grid: list[str]) -> list[int]:
        m, n = len(grid), len(grid[0])
        
        @cache
        def work(i, j):
            if i == m or j == n or grid[i][j] == 'X':
                return (-inf, 0)
            if grid[i][j] == 'S':
                return (0, 1)

            x, y = -inf, 0
            for ii, jj in [(i + 1, j), (i, j + 1), (i + 1, j + 1)]:
                xx, yy = work(ii, jj)
                if xx > x:
                    x, y = xx, yy
                elif xx == x:
                    y = (y + yy) % (10 ** 9 + 7)
            return x + (0 if grid[i][j] == 'E' else int(grid[i][j])), y

        return (0, 0) if work(0, 0)[0] < 0 else work(0, 0)
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
