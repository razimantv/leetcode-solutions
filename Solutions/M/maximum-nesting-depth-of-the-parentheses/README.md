# Maximum nesting depth of the parentheses

[Problem link](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        ret, cur = 0, 0
        for c in s:
            cur += 1 if c == '(' else -1 if c == ')' else 0
            ret = max(ret, cur)
        return ret
```
## Tags

* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum) > [Valid brackets](/README.md#Prefix-Sum-Valid_brackets)
