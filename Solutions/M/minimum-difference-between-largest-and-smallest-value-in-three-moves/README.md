# Minimum difference between largest and smallest value in three moves

[Problem link](https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        return min(nums[i+n-4] - nums[i] for i in range(4))
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
