# Smallest index with digit sum equal to index

[Problem link](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/


class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i, x in enumerate(nums):
            if sum(map(int, str(x))) == i:
                return i
        return -1
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
