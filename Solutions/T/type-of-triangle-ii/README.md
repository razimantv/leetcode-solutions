# Type of triangle ii

[Problem link](https://leetcode.com/problems/type-of-triangle-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/type-of-triangle-ii/

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums = sorted(nums)
        if nums[0] == nums[2]:
            return "equilateral"
        elif nums[0] + nums[1] <= nums[2]:
            return "none"
        elif nums[1] in [nums[0], nums[2]]:
            return "isosceles"
        else:
            return "scalene"
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Geometry](/Collections/mathematics.md#geometry)
