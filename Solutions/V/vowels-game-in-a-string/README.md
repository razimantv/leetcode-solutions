# Vowels game in a string

[Problem link](https://leetcode.com/problems/vowels-game-in-a-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/vowels-game-in-a-string/

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return True if any(c for c in 'aeiou' if c in s) else False
```
## Tags

* [Two player games](/Collections/two-player-games.md#two-player-games)
