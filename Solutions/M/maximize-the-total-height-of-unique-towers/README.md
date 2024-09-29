# Maximize the total height of unique towers

[Problem link](https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        ret, large = 0, 1 << 30
        for x in sorted(maximumHeight, reverse=True):
            large = min(x, large - 1)
            if not large:
                return -1
            ret += large
        return ret
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
