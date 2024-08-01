# Score after flipping matrix

[Problem link](https://leetcode.com/problems/score-after-flipping-matrix/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/score-after-flipping-matrix/

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ret = 0
        for i in range(len(grid[0])):
            ctr = Counter(row[0] ^ row[i] for row in grid)
            ret = ret * 2 + max(ctr.values())
        return ret
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Greedy](/Collections/greedy.md#greedy)
