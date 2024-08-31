# Minimum amount of damage dealt to bob

[Problem link](https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

class Solution:
    def minDamage(
        self, power: int, damage: List[int], health: List[int]
    ) -> int:
        time = [(h + power - 1) // power for h in health]
        idx = sorted(
            list(range(len(damage))), key=lambda i: time[i] / damage[i]
        )

        t, ret = 0, 0
        for x in idx:
            t += time[x]
            ret += damage[x] * t
        return ret
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Sorting](/Collections/sorting.md#sorting) > [Index array](/Collections/sorting.md#index-array)
