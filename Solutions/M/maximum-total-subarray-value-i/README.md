# Maximum total subarray value i

[Problem link](https://leetcode.com/problems/maximum-total-subarray-value-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-total-subarray-value-i/

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        return (max(nums) - min (nums)) * k
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
