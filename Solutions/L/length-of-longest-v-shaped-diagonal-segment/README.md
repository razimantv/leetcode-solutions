# Length of longest v shaped diagonal segment

[Problem link](https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        neigh = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        def get(i, j):
            return grid[i][j] if 0 <= i < m and 0 <= j < n else -1

        @cache
        def dp(i, j, dir, steps):
            if not steps:
                return 0
            cur, add = 1, 0
            for dstep in (0, 1):
                if get(
                    ii := (i + neigh[dir][0]), jj := (j + neigh[dir][1])
                ) == 2 - grid[i][j]:
                    add = max(add, dp(ii, jj, dir, steps - dstep))
                dir = (dir + 1) & 3
            return cur + add

        ret = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if grid[i][j] != 1:
                    continue
                cur, add = 1, 0
                for dir, (di, dj) in enumerate(neigh):
                    if get(ii := (i + di), jj := (j + dj)) == 2:
                        add = max(add, dp(ii, jj, dir, 2))
                ret = max(ret, cur + add)

        return ret
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
