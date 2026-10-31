# Twisted mirror path count

[Problem link](https://leetcode.com/problems/twisted-mirror-path-count/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/twisted-mirror-path-count/

class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def cnt(i, j, dir):
            if i == m or j == n:
                return 0
            elif (i, j) == (m - 1, n - 1):
                return 1
            elif grid[i][j]:
                return cnt(i + 1, j, 0) if dir else cnt(i, j + 1, 1)
            else:
                return (cnt(i + 1, j, 0) + cnt(i, j + 1, 1)) % (10 ** 9 + 7)
        return cnt(0, 0, 0)
```
## Tags

* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
