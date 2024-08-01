# Minimum operations to exceed threshold value i

[Problem link](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return len([x for x in nums if x < k])
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
