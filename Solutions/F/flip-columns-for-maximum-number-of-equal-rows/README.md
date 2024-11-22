# Flip columns for maximum number of equal rows

[Problem link](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        return max(Counter(
            tuple(i ^ row[0] for i in row) for row in matrix
        ).values())
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
