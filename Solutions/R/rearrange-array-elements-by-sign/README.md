# Rearrange array elements by sign

[Problem link](https://leetcode.com/problems/rearrange-array-elements-by-sign/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)
        pos = [0, 1]
        for x in nums:
            idx = 0 if x > 0 else 1
            ret[pos[idx]] = x
            pos[idx] += 2
        return ret
```
## Tags

* [Two pointers](/Collections/two-pointers.md#two-pointers)
