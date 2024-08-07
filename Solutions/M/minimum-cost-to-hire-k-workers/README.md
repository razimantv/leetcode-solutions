# Minimum cost to hire k workers

[Problem link](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = sorted(list(zip(wage, quality)), key=lambda x: x[0] / x[1])
        heap, tot, ret = [], 0, math.inf
        for w, q in pairs:
            heapq.heappush(heap, -q)
            tot += q
            if len(heap) > k:
                tot += heapq.heappop(heap)
            if len(heap) == k:
                ret = min(ret, tot * w / q)
        return ret
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue) > [K smallest/largest elements](/Collections/priority-queue.md#k-smallest-largest-elements)
