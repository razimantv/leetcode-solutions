# Maximum frequency of an element after performing operations i

[Problem link](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        ends = sorted([
            (x + i * k, i) for x in nums for i in [-1, 0, 1]
        ])
        cnt, cur, curcnt, ret = 0, 10 ** 10, 0, 0
        for x, delta in ends:
            if delta == 0:
                if cur != x:
                    cur, curcnt = x, 0
                curcnt += 1
            else:
                curcnt = 0
            cnt -= delta
            other = cnt - curcnt
            ret = max(ret, curcnt + min(numOperations, other))
        return ret
```
## Tags

* [Intervals](/Collections/intervals.md#intervals) > [Endpoint sorting](/Collections/intervals.md#endpoint-sorting)
* [Intervals](/Collections/intervals.md#intervals) > [Overlap](/Collections/intervals.md#overlap)
