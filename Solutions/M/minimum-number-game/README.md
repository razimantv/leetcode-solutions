# Minimum number game

[Problem link](https://leetcode.com/problems/minimum-number-game/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-game/

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
