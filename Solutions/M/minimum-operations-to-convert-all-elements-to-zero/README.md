# Minimum operations to convert all elements to zero

[Problem link](https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        mono, ret = [-1], 0
        for x in nums:
            while mono[-1] > x:
                mono.pop()
            if mono[-1] < x:
                mono.append(x)
                ret += (x > 0)
        return ret
```
## Tags

* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
