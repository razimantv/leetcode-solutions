# Most profit assigning work

[Problem link](https://leetcode.com/problems/most-profit-assigning-work/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        job, n, l = sorted(zip(difficulty, profit)), len(profit), 0
        best, ret = 0, 0
        for x in sorted(worker):
            while l < n and job[l][0] <= x:
                best = max(best, job[l][1])
                l += 1
            ret += best
        return ret
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Two pointers](/Collections/two-pointers.md#two-pointers)
