# Minimum processing time

[Problem link](https://leetcode.com/problems/minimum-processing-time/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, time: List[int], tasks: List[int]) -> int:
        tasks = sorted(tasks)
        time = sorted(time)
        ret = 0
        for i, t in enumerate(time[::-1]):
            ret = max(ret, t + tasks[i*4+3])
        return ret
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
