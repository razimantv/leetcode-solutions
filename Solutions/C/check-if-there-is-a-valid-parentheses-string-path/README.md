# Check if there is a valid parentheses string path

[Problem link](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/


class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        if grid[0][0] != "(":
            return False
        grid[0][0] = {1}
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if not i + j:
                    continue
                add = 1 if c == "(" else -1
                prev = set()
                if i:
                    prev.update(grid[i - 1][j])
                if j:
                    prev.update(grid[i][j - 1])
                grid[i][j] = {add + x for x in prev if add + x >= 0}
        return 0 in grid[-1][-1]
```
## Tags

* [Matrix](/Collections/matrix.md#matrix) > [Numpy](/Collections/matrix.md#numpy)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Grid](/Collections/dynamic-programming.md#grid)
