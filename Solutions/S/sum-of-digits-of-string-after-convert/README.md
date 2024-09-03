# Sum of digits of string after convert

[Problem link](https://leetcode.com/problems/sum-of-digits-of-string-after-convert/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        if k == 0:
            return int(s)
        s = ''.join(
            c if c <= '9' else str(ord(c) - ord('a') + 1)
            for c in s
        )
        s = str(sum(int(c) for c in s))
        return self.getLucky(s, k - 1)
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
