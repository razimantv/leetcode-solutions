# Zero array transformation ii

[Problem link](https://leetcode.com/problems/zero-array-transformation-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)

        def poss(k):
            pref = [0] * (n+1)
            for l, r, delta in queries[:k]:
                pref[l] += delta
                pref[r+1] -= delta
            cur = 0
            for x, y in zip(nums, pref):
                cur += y
                if x > cur:
                    return False
            return True

        start, end = -1, q + 1
        while end - start > 1:
            mid = (start + end) // 2
            if poss(mid):
                end = mid
            else:
                start = mid
        return -1 if end > q else end
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [For range updates](/Collections/prefix.md#for-range-updates)
