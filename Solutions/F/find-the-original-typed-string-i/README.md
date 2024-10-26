# Find the original typed string i

[Problem link](https://leetcode.com/problems/find-the-original-typed-string-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-original-typed-string-i/

class Solution:
    def possibleStringCount(self, word: str) -> int:
        return 1 + sum(x == y for x, y in pairwise(word))
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
