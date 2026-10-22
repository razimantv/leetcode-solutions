# Minimum operations to sort a permutation

[Problem link](https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        if (n := len(nums)) == 1:
            return 0
        diffs = list({(y + n - x) % n for x, y in pairwise(nums)})
        if len(diffs) != 1 or (diffs[0] not in [1, n - 1]):
            return -1
        z = next(i for i, x in enumerate(nums) if x == 0)
        if diffs[0] == 1:
            return min(z, n + 2 - z)
        else:
            return 1 + min(n - 1 - z, z + 1)
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
* [Case-by-case analysis](/Collections/case-by-case-analysis.md#case-by-case-analysis)
* [Array scanning](/Collections/array-scanning.md#array-scanning)
