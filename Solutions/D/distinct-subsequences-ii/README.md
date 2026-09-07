# Distinct subsequences ii

[Problem link](https://leetcode.com/problems/distinct-subsequences-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/distinct-subsequences-ii/

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp, mod, ret = [1], 10 ** 9 + 7, 0
        for i, c in enumerate(s):
            cur = 0
            for j in range(i, -1, -1):
                cur += dp[j]
                if cur >= mod:
                    cur -= mod
                if j and s[j - 1] == c:
                    break
            ret += cur
            if ret >= mod:
                ret -= mod
            dp.append(cur)
        return ret
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with same value](/Collections/array-scanning.md#location-of-previous-element-with-same-value)
