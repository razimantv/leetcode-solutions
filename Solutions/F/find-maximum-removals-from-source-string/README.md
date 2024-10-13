# Find maximum removals from source string

[Problem link](https://leetcode.com/problems/find-maximum-removals-from-source-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-maximum-removals-from-source-string/

class Solution:
    def maxRemovals(
        self, source: str, pattern: str, targetIndices: List[int]
    ) -> int:
        # dp(i, j) = max length of pattern matched up to i characters of source
        # if j indices have been removed
        L, M = len(targetIndices), len(pattern)
        dp = [0] + [-math.inf] * L
        ptr = 0

        for i, c in enumerate(source):
            newdp = [x + (c == pattern[x] if 0 <= x < M else 0) for x in dp]
            if ptr < L and targetIndices[ptr] == i:
                ptr += 1
                for j in range(1, L + 1):
                    newdp[j] = max(newdp[j], dp[j - 1])
            dp = newdp

        for i in range(L, 0, -1):
            if dp[i] == M:
                return i
        return 0
```
## Tags

* [String](/Collections/string.md#string) > [Subsequence](/Collections/string.md#subsequence)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Longest common subsequence](/Collections/dynamic-programming.md#longest-common-subsequence)
