# Minimum bit flips to convert number

[Problem link](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
