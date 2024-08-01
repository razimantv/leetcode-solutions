# Minimum operations to exceed threshold value ii

[Problem link](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ret = 0
        while nums[0] < k:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, 2 * x + y)
            ret += 1
        return ret
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue)
