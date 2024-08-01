# Find the k or of an array

[Problem link](https://leetcode.com/problems/find-the-k-or-of-an-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-k-or-of-an-array/

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        cnt = [0] * 31
        for x in nums:
            for i in range(31):
                if (x & (1 << i)):
                    cnt[i] += 1

        ret = 0
        for i, j in enumerate(cnt):
            if j >= k:
                ret |= (1 << i)
        return ret
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
