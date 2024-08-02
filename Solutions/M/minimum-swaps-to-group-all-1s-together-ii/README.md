# Minimum swaps to group all 1s together ii

[Problem link](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n, psum = len(nums), [0] + list(accumulate(nums + nums))
        ones = psum[-1] // 2
        return ones - max(psum[i + ones] - psum[i] for i in range(n))
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Cyclic array](/Collections/array-scanning.md#cyclic-array)
