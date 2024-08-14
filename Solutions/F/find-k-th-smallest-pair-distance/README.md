# Find k th smallest pair distance

[Problem link](https://leetcode.com/problems/find-k-th-smallest-pair-distance/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n, nums = len(nums), sorted(nums)

        def cnt(x):
            l, ret = 0, 0
            for r in range(n):
                while l < r and nums[r] - nums[l] > x:
                    l += 1
                ret += r - l
            return ret

        start, end = -1, nums[-1] - nums[0]
        while end - start > 1:
            mid = (start + end) // 2
            if cnt(mid) >= k:
                end = mid
            else:
                start = mid
        return end
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Sliding window](/Collections/sliding-window.md#sliding-window)
