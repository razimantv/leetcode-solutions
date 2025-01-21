# Grid game

[Problem link](https://leetcode.com/problems/grid-game)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/grid-game

class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        psum = [[0] + list(accumulate(row)) for row in grid]
        return min(
            max(psum[0][-1] - psum[0][i + 1], psum[1][i] - psum[1][0])
            for i in range(len(grid[0]))
        )
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
