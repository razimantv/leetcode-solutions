# Sum game

[Problem link](https://leetcode.com/problems/sum-game/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/sum-game/

class Solution:
    def sumGame(self, num: str) -> bool:
        n, diff, q = len(num) // 2, 0, 0
        for i, c in enumerate(num):
            if c == '?':
                q += 1
                diff += 9 if i < n else 0
            else:
                diff += int(c) * (1 if i < n else -1)
        return diff * 2 != 9 * q
```
## Tags

* [Two player games](/Collections/two-player-games.md#two-player-games)
