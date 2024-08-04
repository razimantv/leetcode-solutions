# Design neighbor sum service

[Problem link](https://leetcode.com/problems/design-neighbor-sum-service/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/design-neighbor-sum-service/

class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.pos = [0] * (self.n ** 2)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                self.pos[x] = (i, j)

    def adjacentSum(self, value: int) -> int:
        i, j = self.pos[value]
        ret = 0
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ii, jj = i + di, j + dj
            if 0 <= ii < self.n and 0 <= jj < self.n:
                ret += self.grid[ii][jj]
        return ret

    def diagonalSum(self, value: int) -> int:
        i, j = self.pos[value]
        ret = 0
        for di, dj in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            ii, jj = i + di, j + dj
            if 0 <= ii < self.n and 0 <= jj < self.n:
                ret += self.grid[ii][jj]
        return ret
```
## Tags

* [Matrix](/Collections/matrix.md#matrix)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Forward and backward](/Collections/hashmap.md#forward-and-backward)
