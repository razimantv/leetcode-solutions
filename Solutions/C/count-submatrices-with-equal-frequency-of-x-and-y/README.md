# Count submatrices with equal frequency of x and y

[Problem link](https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        xpref = [[0] * n for _ in range(m)]
        ypref = [[0] * n for _ in range(m)]
        ret = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                xpref[i][j] = (
                    (xpref[i-1][j] if i else 0) + (xpref[i][j-1] if j else 0) -
                    (xpref[i-1][j-1] if i and j else 0) + (grid[i][j] == 'X')
                )
                ypref[i][j] = (
                    (ypref[i-1][j] if i else 0) + (ypref[i][j-1] if j else 0) -
                    (ypref[i-1][j-1] if i and j else 0) + (grid[i][j] == 'Y')
                )
                if xpref[i][j] and xpref[i][j] == ypref[i][j]:
                    ret += 1
        return ret
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [2D](/Collections/prefix.md#2d)
* [Matrix](/Collections/matrix.md#matrix) > [Prefix](/Collections/matrix.md#prefix)
