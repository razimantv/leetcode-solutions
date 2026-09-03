# Construct uniform parity array ii

[Problem link](https://leetcode.com/problems/construct-uniform-parity-array-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/construct-uniform-parity-array-ii/

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        cnt = Counter(x & 1 for x in nums1)
        return bool((len(cnt) == 1) or (min(nums1) & 1))
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Parity](/Collections/mathematics.md#parity)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
