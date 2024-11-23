# Zero array transformation iii

[Problem link](https://leetcode.com/problems/zero-array-transformation-iii)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/zero-array-transformation-iii

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        q, queries = len(queries), sorted(queries)
        fixed, free = [], []
        p, forced = 0, 0
        for i, x in enumerate(nums):
            while p < q and queries[p][0] <= i:
                heappush(free, -queries[p][1])
                p += 1
            while fixed and fixed[0] < i:
                heappop(fixed)
            while x > len(fixed) and free:
                r = -heappop(free)
                if r >= i:
                    forced += 1
                    heappush(fixed, r)
            if x > len(fixed):
                return -1
        return q - forced
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
* [Intervals](/Collections/intervals.md#intervals)
