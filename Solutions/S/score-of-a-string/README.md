# Score of a string

[Problem link](https://leetcode.com/problems/score-of-a-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/score-of-a-string/

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(c)-ord(d)) for c, d in pairwise(s))
```
## Tags

* [Simple implementation](/README.md#Simple_implementation)
