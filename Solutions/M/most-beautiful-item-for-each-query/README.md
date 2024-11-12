# Most beautiful item for each query

[Problem link](https://leetcode.com/problems/most-beautiful-item-for-each-query/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/most-beautiful-item-for-each-query/

class Solution:
    def maximumBeauty(
        self, items: List[List[int]], queries: List[int]
    ) -> List[int]:
        items.sort()
        n, l, best = len(items), 0, 0
        for q, i in sorted([(q, i) for i, q in enumerate(queries)]):
            while l < n and items[l][0] <= q:
                best = max(best, items[l][1])
                l += 1
            queries[i] = best
        return queries
```
## Tags

* [Two pointers](/Collections/two-pointers.md#two-pointers)
* [Sorting](/Collections/sorting.md#sorting) > [Remembering index](/Collections/sorting.md#remembering-index)
