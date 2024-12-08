# Maximum subarray sum with length divisible by k

[Problem link](https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n, ret = len(nums), -math.inf
        psum = [0] + list(accumulate(nums))
        for i in range(k):
            low = psum[i]
            for j in range(i + k, n + 1, k):
                ret = max(ret, psum[j] - low)
                low = min(psum[j], low)
        return ret
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Array scanning](/Collections/array-scanning.md#array-scanning)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
