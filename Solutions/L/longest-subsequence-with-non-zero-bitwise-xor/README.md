# Longest subsequence with non zero bitwise xor

[Problem link](https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        if max(nums) == 0:
            return 0
        elif reduce(xor, nums):
            return len(nums)
        else:
            return len(nums) - 1
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
