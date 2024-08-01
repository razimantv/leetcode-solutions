# Relative sort array

[Problem link](https://leetcode.com/problems/relative-sort-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos = {x: i for i, x in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (pos.get(x, 1001), x))
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
