# Count alternating subarrays

[Problem link](https://leetcode.com/problems/count-alternating-subarrays/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-alternating-subarrays/

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ret, cur = 0, 0
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                cur = 1
            else:
                cur += 1
            ret += cur
        return ret
```
## Tags

* [Array scanning](/README.md#Array_scanning) > [Contiguous region](/README.md#Array_scanning-Contiguous_region)
