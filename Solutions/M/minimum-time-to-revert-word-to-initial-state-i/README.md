# Minimum time to revert word to initial state i

[Problem link](https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        p1, MOD = 43, 10 ** 9 + 7

        n = len(word)
        fwhash, bwhash = [0] * n, [0] * n

        cur = 0
        for i in range(n):
            cur = (cur * p1 + ord(word[i]) - ord('a')) % MOD
            fwhash[i] = cur

        cur, mult = 0, 1
        for i in range(n - 1, -1, -1):
            cur = (cur + mult * (ord(word[i]) - ord('a'))) % MOD
            bwhash[i] = cur
            mult = (mult * p1) % MOD

        ret, start = 1, k
        while start < n:
            if bwhash[start] == fwhash[n - 1 - start]:
                return ret
            ret += 1
            start += k

        return ret
```
## Tags

* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Hashing](/Collections/string.md#hashing)
