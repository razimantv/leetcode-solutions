# Minimum moves to make array complementary

[Problem link](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        n, pref = len(nums), [0] * (2 * limit + 2)
        for i in range(n // 2):
            a, b = sorted([nums[i], nums[n-1-i]])
            pref[0] += 2
            pref[a+1] -= 1
            pref[a+b] -= 1
            pref[a+b+1] += 1
            pref[b+limit+1] += 1
        return min(accumulate(pref))
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [For range updates](/Collections/prefix.md#for-range-updates)
* [Range updates using prefix sum](/Collections/range-updates-using-prefix-sum.md#range-updates-using-prefix-sum)
