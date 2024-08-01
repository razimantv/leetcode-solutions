# Find the first player to win k games in a row

[Problem link](https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n, cnt = len(skills), 0
        indices = list(range(n))
        for i in range(n - 1):
            if skills[indices[i]] > skills[indices[i + 1]]:
                indices[i], indices[i + 1] = indices[i + 1], indices[i]
                cnt += 1
            else:
                cnt = 1
            if cnt == k:
                return indices[i + 1]

        return indices[-1]
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
