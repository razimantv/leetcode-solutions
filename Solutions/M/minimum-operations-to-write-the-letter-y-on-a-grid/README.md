# Minimum operations to write the letter y on a grid

[Problem link](https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid) // 2
        ctr_all = Counter(sum(grid, start=[]))
        ctr_y = Counter([
            grid[n][n]] +
            sum(
                (
                    [grid[i][i], grid[i][2 * n - i], grid[2 * n - i][n]]
                    for i in range(n)
                ), start=[]
            )
        )

        ret = 9 * n ** 2
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                ret = min(
                    ret,
                    sum(ctr_y[x] for x in range(3) if x != i) +
                    sum(ctr_all[x] - ctr_y[x] for x in range(3) if x != j)
                )

        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
