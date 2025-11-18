# 1 bit and 2 bit characters

[Problem link](https://leetcode.com/problems/1-bit-and-2-bit-characters/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/1-bit-and-2-bit-characters/

class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n, i = len(bits), 0

        while i < n:
            if i == n - 1:
                return True
            i += bits[i] + 1
        return False
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
