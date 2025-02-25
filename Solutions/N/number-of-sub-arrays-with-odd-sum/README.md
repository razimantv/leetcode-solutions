# Number of sub arrays with odd sum

[Problem link](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ctr = Counter(x & 1 for x in list(accumulate(arr)))
        return ((ctr[0] + 1) * ctr[1]) % (10 ** 9 + 7)
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Parity](/Collections/mathematics.md#parity)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
