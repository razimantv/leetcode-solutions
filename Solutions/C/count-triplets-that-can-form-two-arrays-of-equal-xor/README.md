# Count triplets that can form two arrays of equal xor

[Problem link](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cnt, tot, cur, ret = {0: 1}, {0: -1}, 0, 0
        for i, x in enumerate(arr):
            cur ^= x
            pcnt, ptot = cnt.get(cur, 0), tot. get(cur, 0)
            ret += pcnt * (i - 1) - ptot
            cnt[cur], tot[cur] = pcnt + 1, ptot + i
        return ret
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Bitwise operation](/Collections/prefix.md#bitwise-operation)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
