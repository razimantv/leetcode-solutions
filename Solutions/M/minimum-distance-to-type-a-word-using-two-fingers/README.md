# Minimum distance to type a word using two fingers

[Problem link](https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(i, j):
            return abs(i // 6 - j // 6) + abs(i % 6 - j % 6)

        dp = [0] * 26
        for c, d in pairwise((ord(x) - ord('A') for x in word)):
            if c == d:
                continue
            cd, best = dist(c, d), min(dp[x] + dist(x, d) for x in range(26))
            dp = [cd + x for x in dp]
            dp[c] = min(dp[c], best)
        return min(dp)
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
