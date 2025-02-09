# Sort matrix by diagonals

[Problem link](https://leetcode.com/problems/sort-matrix-by-diagonals/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/sort-matrix-by-diagonals/

class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        for diff in range(-n, n + 1):
            terms = sorted(
                [grid[i][i - diff] for i in range(n) if 0 <= i - diff < n],
                reverse=diff >= 0
            )
            next = 0
            for i in range(n):
                if 0 <= (j := i - diff) < n:
                    grid[i][j] = terms[next]
                    next += 1
        return grid
```
## Tags

* [Matrix](/Collections/matrix.md#matrix)
