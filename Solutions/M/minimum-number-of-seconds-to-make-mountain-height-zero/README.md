# Minimum number of seconds to make mountain height zero

[Problem link](https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

class Solution:
    def minNumberOfSeconds(
        self, mountainHeight: int, workerTimes: List[int]
    ) -> int:
        def work(x):
            h = mountainHeight
            for t in workerTimes:
                n, y = 1, x
                while h and n * t <= y:
                    h -= 1
                    y -= n * t
                    n += 1
            return not h

        start, end = 0, mountainHeight * \
            (mountainHeight + 1) * min(workerTimes) // 2
        while end - start > 1:
            mid = (start + end) // 2
            if work(mid):
                end = mid
            else:
                start = mid
        return end
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
