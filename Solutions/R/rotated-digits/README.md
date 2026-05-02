# Rotated digits

[Problem link](https://leetcode.com/problems/rotated-digits/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/rotated-digits/

class Solution:
    def rotatedDigits(self, n: int) -> int:
        return sum(
            1 for i in map(str, range(1, n + 1)) if (
                any(c in i for c in '2569') and
                not any(c in i for c in '347')
            )
        )
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
