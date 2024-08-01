# Magnetic force between two balls

[Problem link](https://leetcode.com/problems/magnetic-force-between-two-balls/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def work(d):
            prev, cnt = -d, 0
            for x in position:
                if x - prev >= d:
                    prev = x
                    if (cnt := cnt + 1) == m:
                        return True
            return False

        start, end = 1, (position[-1] - position[0]) // (m - 1) + 1
        while end - start > 1:
            mid = (end + start) // 2
            if work(mid):
                start = mid
            else:
                end = mid
        return start
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Greedy](/Collections/greedy.md#greedy)
