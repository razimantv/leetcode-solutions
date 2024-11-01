# Delete characters to make fancy string

[Problem link](https://leetcode.com/problems/delete-characters-to-make-fancy-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        return ''.join(c for i, c in enumerate(s) if s[i:i+3] != c * 3)
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
