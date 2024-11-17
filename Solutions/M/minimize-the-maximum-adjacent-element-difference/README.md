# Minimize the maximum adjacent element difference

[Problem link](https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n, ar, d, last = len(nums), [], 0, -100
        for i, x in enumerate(nums):
            if x == -1:
                continue
            if i == 0:
                pass
            elif last == i - 1:
                d = max(d, abs(x - nums[last]))
            elif last == -100 or x == nums[last]:
                ar += [[x, x, 1]]
            else:
                ar += [sorted([nums[last], x]) + [1 + (last < i - 2)]]
            last = i
        if last == -100 or not ar:
            return d
        if last != n-1:
            ar += [[nums[last], nums[last], 1]]
        big, small = max(y for _, y, _ in ar), min(x for x, _, _ in ar)

        start = d - 1
        end = max(start + 1, (big - small + 1) // 2)

        def work(d):
            x, y = small + d, big - d
            for z1, z2, g in ar:
                if min(
                    max(abs(z-t) for z in (z1, z2)) for t in (x, y)
                ) > d and (
                    g == 1 or y - x > d or max(abs(z1 - x), abs(z2 - y)) > d
                ):
                    return False
            return True

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
* [Greedy](/Collections/greedy.md#greedy)
