# Robot return to origin

[Problem link](https://leetcode.com/problems/robot-return-to-origin/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dr = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}
        x, y = 0, 0
        for m in moves:
            x, y = x + dr[m][0], y + dr[m][1]
        return (x == 0) and (y == 0)
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
