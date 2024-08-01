# Sort integers by the number of 1 bits

[Problem link](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (x.bit_count(), x))
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
