# Unique 3 digit even numbers

[Problem link](https://leetcode.com/problems/unique-3-digit-even-numbers/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/unique-3-digit-even-numbers/

class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        return len(set([
            x for x in permutations(digits, 3) if x[0] and (x[-1] % 2 == 0)
        ]))
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
