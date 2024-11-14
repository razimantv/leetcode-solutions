# Minimized maximum of products distributed to any store

[Problem link](https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def poss(x):
            return sum((q + x - 1) // x for q in quantities) <= n

        start, end = 0, max(quantities)
        while end - start > 1:
            mid = (end + start) // 2
            if poss(mid):
                end = mid
            else:
                start = mid
        return end
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
