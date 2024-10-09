# Minimum add to make parentheses valid

[Problem link](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left, right = 0, 0
        for c in s:
            if c == '(':
                right += 1
            elif right:
                right -= 1
            else:
                left += 1
        return left + right
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [Valid brackets](/Collections/prefix.md#valid-brackets)
