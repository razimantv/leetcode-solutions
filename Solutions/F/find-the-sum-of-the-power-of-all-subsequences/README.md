# Find the sum of the power of all subsequences

[Problem link](https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [[0] * (n + 1) for _ in range(k + 1)]
        cnt[0][0] = 1

        MOD = 10 ** 9 + 7
        for i, x in enumerate(nums):
            for l in range(i, -1, -1):
                for j in range(k):
                    jj = j + x
                    if jj <= k:
                        cnt[jj][l + 1] = (cnt[jj][l + 1] + cnt[j][l]) % MOD

        ret, mult = 0, 1
        for l in range(n, 0, -1):
            ret = (ret + cnt[k][l] * mult) % MOD
            mult = (mult << 1) % MOD
        return ret
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Knapsack](/Collections/dynamic-programming.md#knapsack)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
