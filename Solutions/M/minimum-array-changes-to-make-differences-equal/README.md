# Minimum array changes to make differences equal

[Problem link](https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        pref = [0] * (k + 2)
        n = len(nums) // 2
        for i in range(n):
            x, y = nums[i], nums[-1-i]
            if x > y:
                x, y = y, x
            z = y - x
            pref[0] += 1
            pref[z] -= 1
            pref[z + 1] += 1
            pref[max(y, k - x) + 1] += 1
        return min(accumulate(pref))
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [For range updates](/Collections/prefix.md#for-range-updates)
