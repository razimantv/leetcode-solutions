# Maximum xor score subarray queries

[Problem link](https://leetcode.com/problems/maximum-xor-score-subarray-queries/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-xor-score-subarray-queries/

class Solution:
    def maximumSubarrayXor(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(nums)
        sxor, dp = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]
        for i in range(n):
            sxor[i][i] = dp[i][i] = nums[i]

        for L in range(2, n + 1):
            i, j = 0, L - 1
            while j < n:
                sxor[i][j] = sxor[i][j - 1] ^ sxor[i + 1][j]
                dp[i][j] = max(sxor[i][j], dp[i][j - 1], dp[i + 1][j])
                i, j = i + 1, j + 1

        return [dp[i][j] for i, j in queries]
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Length-wise processing](/Collections/dynamic-programming.md#length-wise-processing)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Auxiliary array](/Collections/dynamic-programming.md#auxiliary-array)
