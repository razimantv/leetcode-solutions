# Minimum limit of balls in a bag

[Problem link](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def work(y):
            return sum((x - 1) // y for x in nums) <= maxOperations

        start, end = 0, max(nums)
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
