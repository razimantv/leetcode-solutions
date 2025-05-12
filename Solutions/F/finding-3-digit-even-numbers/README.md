# Finding 3 digit even numbers

[Problem link](https://leetcode.com/problems/finding-3-digit-even-numbers/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/finding-3-digit-even-numbers/

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        return sorted(list(set(
            100 * a + 10 * b + c for a, b, c in permutations(digits, 3)
            if a and not (c & 1)
        )))
```
## Tags

* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration)
