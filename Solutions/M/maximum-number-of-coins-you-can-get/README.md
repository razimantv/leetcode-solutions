# Maximum number of coins you can get

[Problem link](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles = sorted(piles)
        return sum(piles[3*n - 2*i] for i in range(1, n+1))
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
