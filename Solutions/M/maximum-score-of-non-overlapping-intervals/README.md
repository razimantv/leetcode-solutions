# Maximum score of non overlapping intervals

[Problem link](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = sorted([
            [e, s, v, i] for i, (s, e, v) in enumerate(intervals)
        ])
        dp = [[[0, []] for _ in range(5)]]
        for i, (e, s, v, idx) in enumerate(intervals):
            dp.append([[0, []]])
            prev = bisect_left(intervals, [s])
            for j in range(1, 5):
                dp[-1].append(min(
                    dp[-2][j],
                    [dp[prev][j-1][0] - v, sorted(dp[prev][j-1][1] + [idx])]
                ))
        return min(dp[-1])[1]
```
## Tags

* [Intervals](/Collections/intervals.md#intervals) > [Dynamic programming](/Collections/intervals.md#dynamic-programming) > [With binary search](/Collections/intervals.md#with-binary-search)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Intervals](/Collections/dynamic-programming.md#intervals)
* [Sorting](/Collections/sorting.md#sorting) > [Remembering index](/Collections/sorting.md#remembering-index)
