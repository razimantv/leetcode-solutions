# Identify the largest outlier in an array

[Problem link](https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        tot, ctr = sum(nums), Counter(nums)
        for x in sorted(nums):
            rest = tot - x
            if rest % 2 == 0 and ctr[rest // 2] > (rest // 2 == x):
                ret = x
        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
