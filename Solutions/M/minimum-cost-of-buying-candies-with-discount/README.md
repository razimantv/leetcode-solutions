# Minimum cost of buying candies with discount

[Problem link](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        return sum(
            (x for i, x in enumerate(sorted(cost, reverse=True)) if i % 3 != 2)
        )
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
