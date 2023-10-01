# Minimum size subarray in infinite array

[Problem link](https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        tot = sum(nums)
        add = (target // tot) * len(nums)
        target %= tot
        nums += nums

        seen = {0: -1}
        pref, best = 0, -1
        for i, x in enumerate(nums):
            pref += x
            seen[pref] = i
            if pref - target in seen:
                length = i - seen[pref-target]
                if best == -1 or best > length:
                    best = length

        return -1 if best == -1 else best+add
```
## Tags

* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum)
* [Dynamic programming](/README.md#Dynamic_programming) > [Cyclic array](/README.md#Dynamic_programming-Cyclic_array)
