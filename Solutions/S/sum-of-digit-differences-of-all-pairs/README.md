# Sum of digit differences of all pairs

[Problem link](https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n, nums = len(nums), [str(x) for x in nums]
        ret = 0
        for i in range(len(nums[0])):
            ctr = Counter(x[i] for x in nums)
            ret += n * (n - 1) // 2 - sum(
                x * (x - 1) // 2 for x in ctr.values()
            )
        return ret
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
