# Maximum alternating sum of squares

[Problem link](https://leetcode.com/problems/maximum-alternating-sum-of-squares/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/

class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares, n = sorted([x ** 2 for x in nums]), len(nums)
        return sum(squares[n // 2:]) - sum(squares[:n // 2])
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
