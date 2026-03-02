# Minimum swaps to arrange a binary grid

[Problem link](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n, ret = len(grid), 0
        ar = [
            next((i for i in range(n - 1, -1, -1) if grid[j][i]), -1)
            for j in range(n)
        ]
        for i in range(n):
            r = next((j for j in range(i, n) if ar[j] <= i), n)
            if r == n:
                return -1
            ret += r - i
            for j in range(r, i, -1):
                ar[j], ar[j - 1] = ar[j - 1], ar[j]
        return ret
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Matrix](/Collections/matrix.md#matrix)
* [Sorting](/Collections/sorting.md#sorting)
