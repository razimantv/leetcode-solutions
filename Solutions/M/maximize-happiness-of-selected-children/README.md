# Maximize happiness of selected children

[Problem link](https://leetcode.com/problems/maximize-happiness-of-selected-children/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximize-happiness-of-selected-children/

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        tot = 0
        for i, x in enumerate(sorted(happiness, reverse=True)[:k]):
            tot += max(x - i, 0)
        return tot
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
