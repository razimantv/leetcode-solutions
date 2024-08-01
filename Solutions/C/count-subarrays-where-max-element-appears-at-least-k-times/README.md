# Count subarrays where max element appears at least k times

[Problem link](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        last = {0: -1}
        cnt, ret = 0, 0
        m = max(nums)
        for i, x in enumerate(nums):
            if x == m:
                cnt += 1
            if cnt >= k:
                ret += last[cnt - k] + 2
            last[cnt] = i
        return ret
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
