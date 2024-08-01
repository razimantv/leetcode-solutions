# Minimum number of days to make m bouquets

[Problem link](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloom: List[int], m: int, k: int) -> int:
        n = len(bloom)
        if m * k > n:
            return -1

        def work(day):
            full, cur = 0, 0
            for x in bloom:
                if x > day:
                    cur = -1
                cur += 1
                if cur == k:
                    cur = 0
                    full += 1
                if full == m:
                    return True
            return False

        start, end = 0, max(bloom)
        while end - start > 1:
            mid = (start + end) >> 1
            if work(mid):
                end = mid
            else:
                start = mid
        return end
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Greedy](/Collections/greedy.md#greedy)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
