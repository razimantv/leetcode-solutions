# Maximum k to sort a permutation

[Problem link](https://leetcode.com/problems/maximum-k-to-sort-a-permutation/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/


class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        ret = (1 << 20) - 1
        for i, x in enumerate(nums):
            if i != x:
                ret &= i
        return 0 if ret > len(nums) else ret
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Permutation](/Collections/permutation.md#permutation) > [Swaps](/Collections/permutation.md#swaps)
