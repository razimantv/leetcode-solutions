# Check if digits are equal in string after operations i

[Problem link](https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(map(int, s))
        while len(s) > 2:
            s = [(x + y) % 10 for x, y in pairwise(s)]
        return s[0] == s[1]
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
