# Reschedule meetings for maximum free time i

[Problem link](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i

class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, start: list[int], end: list[int]
    ) -> int:
        n, psum = len(start), [0] + list(
            accumulate([e - s for s, e in zip(start, end)])
        )
        start.append(eventTime)
        end = [0] + end
        return max(
            start[i] - end[i - k] - psum[i] + psum[i - k]
            for i in range(k, n + 1)
        )
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Sliding window](/Collections/sliding-window.md#sliding-window)
