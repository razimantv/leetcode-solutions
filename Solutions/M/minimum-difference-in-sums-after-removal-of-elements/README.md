# Minimum difference in sums after removal of elements

[Problem link](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 3

        def work(ar, s):
            heap = [s * x for x in ar[:n]]
            heapq.heapify(heap)
            ret = [sum(heap)]
            for x in ar[n:]:
                heapq.heappush(heap, s * x)
                ret.append(ret[-1] + s * x - heapq.heappop(heap))
            return [s * x for x in ret]

        return min((x - y for x, y in zip(
            work(nums[:2 * n], -1), work(nums[-1:n - 1:-1], 1)[::-1]
        )))
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
