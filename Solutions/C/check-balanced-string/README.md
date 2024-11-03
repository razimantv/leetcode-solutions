# Check balanced string

[Problem link](https://leetcode.com/problems/check-balanced-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/check-balanced-string/

class Solution:
    def isBalanced(self, num: str) -> bool:
        return int(num) % 11 == 0
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
