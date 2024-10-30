# Minimum number of removals to make mountain array

[Problem link](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def lis(ar):
            order, ret = [], []
            for x in ar:
                pos = bisect_left(order, x)
                ret.append(pos + 1)
                if pos == len(order):
                    order.append(0)
                order[pos] = x
            return ret

        left, right = lis(nums), lis(nums[::-1])[::-1]
        return len(nums) - max(
            x + y - 1 for x, y in zip(left, right) if min(x, y) > 1
        )
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Longest increasing subsequence](/Collections/dynamic-programming.md#longest-increasing-subsequence)
* [Binary search](/Collections/binary-search.md#binary-search)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
