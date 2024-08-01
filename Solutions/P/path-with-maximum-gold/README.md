# Path with maximum gold

[Problem link](https://leetcode.com/problems/path-with-maximum-gold/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/path-with-maximum-gold/

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dr = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def work(i, j):
            cur, ret = grid[i][j], 0
            grid[i][j] = 0
            for di, dj in dr:
                ii, jj = i + di, j + dj
                if m > ii >= 0 and n > jj >= 0 and grid[ii][jj]:
                    ret = max(ret, work(ii, jj))
            grid[i][j] = cur
            return ret + cur

        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ret = max(ret, work(i, j))
        return ret
```
## Tags

* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
* [Backtracking](/Collections/backtracking.md#backtracking) > [Push and pop for efficient state update](/Collections/backtracking.md#push-and-pop-for-efficient-state-update)
