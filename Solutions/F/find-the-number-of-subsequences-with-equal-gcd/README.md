# Find the number of subsequences with equal gcd

[Problem link](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n, m, mod = len(nums), max(nums) + 1, 10 ** 9 + 7
        dp = [[0] * m for _ in range(m)]
        dp[0][0] = 1

        for x in nums:
            newdp = [[v for v in row] for row in dp]
            for i in range(m):
                for j in range(m):
                    g1, g2 = gcd(i, x), gcd(j, x)
                    newdp[g1][j] = (newdp[g1][j] + dp[i][j]) % mod
                    newdp[i][g2] = (newdp[i][g2] + dp[i][j]) % mod
            dp = newdp

        return sum(dp[i][i] for i in range(1, m)) % mod
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
