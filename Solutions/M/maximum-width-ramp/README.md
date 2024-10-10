# Maximum width ramp

[Problem link](https://leetcode.com/problems/maximum-width-ramp/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-width-ramp/

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ret, mono = 0, []
        for i, v in enumerate(nums):
            pos = bisect_left(mono, -v, key=lambda x: -nums[x])
            if pos == len(mono):
                mono.append(i)
            else:
                ret = max(ret, i - mono[pos])
        return ret
```
## Tags

* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
* [Binary search](/Collections/binary-search.md#binary-search)
