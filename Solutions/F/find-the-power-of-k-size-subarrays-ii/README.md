# Find the power of k size subarrays ii

[Problem link](https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ret = []
        for i, x in enumerate(nums):
            if i and nums[i] == nums[i - 1] + 1:
                cur += 1
            else:
                cur = 1
            if i >= k - 1:
                ret.append(-1 if cur < k else x)
        return ret
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
