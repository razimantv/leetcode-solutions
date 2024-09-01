# Select cells in grid with maximum score

[Problem link](https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        seen = defaultdict(int)
        for i, row in enumerate(grid):
            for x in row:
                seen[x] |= (1 << i)
        seen = list(seen.items())

        @cache
        def best(mask, i):
            if not mask or i < 0:
                return 0
            val, rmask = seen[i]
            rmask &= mask

            ret = best(mask, i - 1)
            while rmask:
                next = rmask & (rmask - 1)
                cur = rmask ^ next
                ret = max(ret, val + best(mask ^ cur, i - 1))
                rmask = next
            return ret

        return best((1 << len(grid)) - 1, len(seen) - 1)
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Subset enumeration](/Collections/bitwise-operation.md#subset-enumeration)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Subsets](/Collections/dynamic-programming.md#subsets)
* [Hashmap](/Collections/hashmap.md#hashmap)
