# Maximum points after enemy battles

[Problem link](https://leetcode.com/problems/maximum-points-after-enemy-battles/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-points-after-enemy-battles/

class Solution:
    def maximumPoints(
        self, enemyEnergies: List[int], currentEnergy: int
    ) -> int:
        low = min(enemyEnergies)
        if currentEnergy < low:
            return 0
        return (currentEnergy + sum(enemyEnergies) - low) // low
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
