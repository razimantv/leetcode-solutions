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

* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
* [Hashmap](/README.md#Hashmap) > [Counter](/README.md#Hashmap-Counter)
