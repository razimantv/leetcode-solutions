# Smallest missing integer greater than sequential prefix sum

[Problem link](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n, tot = len(nums), nums[0]
        for i in range(1, n):
            if nums[i] != nums[i-1] + 1:
                break
            tot += nums[i]

        nums = set(nums)
        while tot in nums:
            tot += 1
        return tot
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
