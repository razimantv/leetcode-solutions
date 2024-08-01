# K th symbol in grammar

[Problem link](https://leetcode.com/problems/k-th-symbol-in-grammar/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return (k-1).bit_count() & 1
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
