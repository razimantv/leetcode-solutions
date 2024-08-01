# Find the maximum length of valid subsequence i

[Problem link](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt, switch, prev = [0, 0], 0, nums[0] - 1
        for x in nums:
            cnt[x & 1] += 1
            if (x + prev) & 1:
                switch += 1
            prev = x
        return max(*cnt, switch)
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
