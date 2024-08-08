# Spiral matrix iii

[Problem link](https://leetcode.com/problems/spiral-matrix-iii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/spiral-matrix-iii/

class Solution:
    def spiralMatrixIII(
        self, m: int, n: int, x: int, y: int
    ) -> List[List[int]]:
        dr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ret = [[x, y]]
        left, step, lim, cur = m * n - 1, 0, 1, 0
        while left:
            dx, dy = dr[step & 3]
            x, y = x + dx, y + dy
            if 0 <= x < m and 0 <= y < n:
                ret.append([x, y])
                left -= 1
            cur += 1
            if cur == lim:
                lim += step & 1
                step += 1
                cur = 0
        return ret
```
## Tags

* [Matrix](/Collections/matrix.md#matrix) > [Traversal](/Collections/matrix.md#traversal)
