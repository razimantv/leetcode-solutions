# Xor after range multiplication queries i

[Problem link](https://leetcode.com/problems/xor-after-range-multiplication-queries-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

class Solution:
    def xorAfterQueries(
        self, nums: list[int], queries: list[list[int]]
    ) -> int:
        for i, j, k, v in queries:
            for x in range(i, j + 1, k):
                nums[x] = (nums[x] * v) % (10 ** 9 + 7)
        return reduce(lambda i, j: i ^ j, nums)
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
