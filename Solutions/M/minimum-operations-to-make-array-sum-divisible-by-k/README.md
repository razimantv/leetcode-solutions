# Minimum operations to make array sum divisible by k

[Problem link](https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
