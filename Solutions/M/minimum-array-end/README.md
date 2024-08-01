# Minimum array end

[Problem link](https://leetcode.com/problems/minimum-array-end/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-array-end/

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        i, n = 0, n - 1
        while n:
            while x & (1 << i):
                i += 1
            if n & 1:
                x |= (1 << i)
            i, n = i + 1, n >> 1
        return x
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
