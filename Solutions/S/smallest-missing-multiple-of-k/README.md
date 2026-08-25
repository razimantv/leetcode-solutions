# Smallest missing multiple of k

[Problem link](https://leetcode.com/problems/smallest-missing-multiple-of-k/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/smallest-missing-multiple-of-k/

class Solution:
    def missingMultiple(self, nums:  list[int], k: int) -> int:
        numsset = set(nums)
        n = k
        while n in numsset:
            n += k
        return n
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
