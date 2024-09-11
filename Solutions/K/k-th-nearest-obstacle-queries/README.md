# K th nearest obstacle queries

[Problem link](https://leetcode.com/problems/k-th-nearest-obstacle-queries/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/k-th-nearest-obstacle-queries/

from sortedcontainers import SortedList


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        sl = SortedList()
        for q, (x, y) in enumerate(queries):
            sl.add(abs(x) + abs(y))
            queries[q] = sl[k - 1] if len(sl) >= k else -1
        return queries
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Python SortedList](/Collections/priority-queue.md#python-sortedlist)