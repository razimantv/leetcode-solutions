# Average waiting time

[Problem link](https://leetcode.com/problems/average-waiting-time/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/average-waiting-time/

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t, wait = 0, 0
        for t0, duration in customers:
            t = max(t, t0) + duration
            wait += t - t0
        return wait / len(customers)
```
## Tags

* [Averaging from total and count](/Collections/averaging-from-total-and-count.md#averaging-from-total-and-count)
