# Remove outermost parentheses

[Problem link](https://leetcode.com/problems/remove-outermost-parentheses/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/remove-outermost-parentheses/


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        a, ret = 0, []
        for c in s:
            b = a + (1 if c == "(" else -1)
            if a * b:
                ret.append(c)
            a = b
        return "".join(ret)
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [Valid brackets](/Collections/prefix.md#valid-brackets)
