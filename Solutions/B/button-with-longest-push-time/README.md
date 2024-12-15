# Button with longest push time

[Problem link](https://leetcode.com/problems/button-with-longest-push-time/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/button-with-longest-push-time/

class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        best = [0, 0]
        last = 0
        for i, t in events:
            best = max(best, [t - last, -i])
            last = t
        return -best[1]
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
