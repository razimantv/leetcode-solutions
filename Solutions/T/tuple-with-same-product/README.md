# Tuple with same product

[Problem link](https://leetcode.com/problems/tuple-with-same-product/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/tuple-with-same-product/

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        ctr = Counter(
            nums[i] * nums[j]
            for i in range(len(nums)) for j in range(i)
        )
        return sum(x * (x - 1) * 4 for x in ctr. values())
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
