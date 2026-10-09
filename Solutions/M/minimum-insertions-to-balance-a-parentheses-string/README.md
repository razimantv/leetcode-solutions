# Minimum insertions to balance a parentheses string

[Problem link](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/


class Solution:
    def minInsertions(self, s: str) -> int:
        n, ret, cnt, part = len(s), 0, 0, 0
        for i, c in enumerate(s):
            if c == "(":
                cnt += 1
            elif part:
                part = 0
                if cnt:
                    cnt -= 1
                else:
                    ret += 1
            elif i < n - 1 and s[i + 1] == c:
                part = 1
            else:
                ret += 1
                if cnt:
                    cnt -= 1
                else:
                    ret += 1
        return ret + 2 * cnt
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [Valid brackets](/Collections/prefix.md#valid-brackets)
