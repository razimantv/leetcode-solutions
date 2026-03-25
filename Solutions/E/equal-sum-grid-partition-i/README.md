# Equal sum grid partition i

[Problem link](https://leetcode.com/problems/equal-sum-grid-partition-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/equal-sum-grid-partition-i/

import numpy as np


class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        for axis in [0, 1]:
            psum = list(accumulate(np.array(grid).sum(axis)))
            if psum[-1] / 2 in psum:
                return True

        return False
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
