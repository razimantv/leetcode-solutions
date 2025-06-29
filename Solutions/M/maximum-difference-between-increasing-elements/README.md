# Maximum difference between increasing elements

[Problem link](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)

## Observations

- The problem asks for the maximum difference `nums[j] - nums[i]` such that `i < j` and `nums[i] < nums[j]`.
- If no such pair `(i, j)` exists, we should return -1.
- This is a classic problem that can be solved by iterating through the array while keeping track of the minimum element found so far.

## Algorithm

The algorithm iterates through the input array `nums` once, maintaining two key variables:

1.  `m`: The minimum value encountered in the array *up to the current position*.
2.  `ret`: The maximum difference found so far that satisfies the conditions.

The process is as follows:

1.  Initialize `ret` to -1 (the value to be returned if no valid difference is found) and `m` to the first element of the array, `nums[0]`.
2.  Iterate through the array `nums` starting from the first element.
3.  For each element `x`:
    -   If `x` is greater than the current minimum `m`, it means we have found a valid pair. We calculate the difference `x - m` and update `ret` to be the maximum of its current value and this new difference.
    -   After checking for the difference, update `m` to be the minimum of its current value and `x`. This ensures that for subsequent elements, we are always comparing against the lowest possible value seen so far.
4.  After the loop finishes, `ret` will hold the maximum difference found, or -1 if no valid pair was ever found.

This approach works because for any `nums[j]`, the maximum possible difference is achieved by subtracting the smallest `nums[i]` where `i < j`. The variable `m` efficiently tracks this minimum value as we iterate.

## Complexity

-   **Time Complexity**: `O(N)`, where `N` is the number of elements in `nums`, because we iterate through the array only once.

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        ret, m = -1, nums[0]
        for x in nums:
            if x > m:
                ret = max(ret, x - m)
            m = min(m, x)
        return ret
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
