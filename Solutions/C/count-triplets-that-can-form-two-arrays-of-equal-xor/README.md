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

* [Prefix](/README.md#Prefix) > [Bitwise operation](/README.md#Prefix-Bitwise_operation)
* [Bitwise operation](/README.md#Bitwise_operation) > [Self-inverse property of xor](/README.md#Bitwise_operation-Self_inverse_property_of_xor)
