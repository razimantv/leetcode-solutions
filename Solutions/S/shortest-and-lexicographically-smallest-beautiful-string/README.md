# Shortest and lexicographically smallest beautiful string

[Problem link](https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        best = ""
        for i in range(n):
            cnt = 0
            cur = ""
            for j in range(i, n):
                cur += s[j]
                if s[j] == "1":
                    cnt += 1
                if cnt == k:
                    break
            else:
                continue

            if not best or len(best) > len(cur) or (
                len(best) == len(cur) and cur < best
            ):
                best = cur + ""
        return best
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
