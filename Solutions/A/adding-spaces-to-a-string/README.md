# Adding spaces to a string

[Problem link](https://leetcode.com/problems/adding-spaces-to-a-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        return ' '.join(s[x:y] for x, y in pairwise([0] + spaces + [len(s)]))
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
