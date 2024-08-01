# Knight dialer

[Problem link](https://leetcode.com/problems/knight-dialer/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/knight-dialer/

class Solution:
    def knightDialer(self, n: int) -> int:
        adj = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9],
               [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        dp = [1] * 10
        MOD = 10 ** 9 + 7
        for i in range(1, n):
            newdp = [0] * 10
            for u in range(10):
                for v in adj[u]:
                    newdp[v] = (newdp[v] + dp[u]) % MOD
            dp = newdp
        return sum(dp) % MOD
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Graph-like state transitions](/Collections/dynamic-programming.md#graph-like-state-transitions)
