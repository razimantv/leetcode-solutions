# Xor queries of a subarray

[Problem link](https://leetcode.com/problems/xor-queries-of-a-subarray/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(
        self, arr: List[int], queries: List[List[int]]
    ) -> List[int]:
        xarr = [0] + list(accumulate(arr, xor))
        return [xarr[r + 1] ^ xarr[l] for l, r in queries]
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Bitwise operation](/Collections/prefix.md#bitwise-operation)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
