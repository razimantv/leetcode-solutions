# Find the winning player in coin game

[Problem link](https://leetcode.com/problems/find-the-winning-player-in-coin-game/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-winning-player-in-coin-game/

class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        return 'Alice' if min(x, y // 4) & 1 else 'Bob'
```
## Tags

* [Two player games](/Collections/two-player-games.md#two-player-games)
