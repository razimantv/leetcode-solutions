# Bitwise ors of subarrays

[Problem link](https://leetcode.com/problems/bitwise-ors-of-subarrays/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/bitwise-ors-of-subarrays/

class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        last, ors = [-1] * 31, set()
        for i, x in enumerate(arr):
            for b in range(30):
                if x & (1 << b):
                    last[b] = i
            y = 0
            ors.add(x)
            for p, q in pairwise(sorted(last, reverse=True)):
                if p != q:
                    y |= arr[p]
                    ors.add(y)
        return len(ors)
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with bit value](/Collections/array-scanning.md#location-of-previous-element-with-bit-value)
