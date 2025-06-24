# Find all k distant indices in an array

[Problem link](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution:
    def findKDistantIndices(
        self, nums: list[int], key: int, k: int
    ) -> list[int]:
        n = len(nums)
        good = [i for i, x in enumerate(nums) if x == key] + [n + k]
        return [i for i in range(n) if good[bisect_left(good, i - k)] <= i + k]
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
