# Maximum total damage with spell casting

[Problem link](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power = sorted(Counter(power).items())
        n = len(power)
        dp = []
        for i, (x, c) in enumerate(power):
            cur = x * c
            best = max(cur, dp[-1] if dp else 0)
            for j in range(i - 1, i - 4, -1):
                if j < 0:
                    break
                elif power[j][0] < x - 2:
                    best = max(best, cur + dp[j])
                    break
            dp.append(best)
        return dp[-1]
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
