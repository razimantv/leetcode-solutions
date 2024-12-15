# Maximum average pass ratio

[Problem link](https://leetcode.com/problems/maximum-average-pass-ratio/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-average-pass-ratio/

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extra: int) -> float:
        def score(p, q):
            return (p - q) / (q * (q + 1))
        classes = [[score(p, q), p, q] for p, q in classes]
        heapify(classes)
        for i in range(extra):
            s, p, q = heappop(classes)
            heappush(classes, [score(p + 1, q + 1), p + 1, q + 1])
        return sum(p / q for _, p, q in classes) / len(classes)
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
