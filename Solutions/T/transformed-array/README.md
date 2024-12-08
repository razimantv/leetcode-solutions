# Transformed array

[Problem link](https://leetcode.com/problems/transformed-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/transformed-array/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[(i + n + nums[i] % n) % n] for i in range(n)]
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Cyclic array](/Collections/array-scanning.md#cyclic-array)
