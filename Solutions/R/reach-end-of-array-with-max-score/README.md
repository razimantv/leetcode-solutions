# Reach end of array with max score

[Problem link](https://leetcode.com/problems/reach-end-of-array-with-max-score/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/reach-end-of-array-with-max-score/

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ret, best = 0, 0
        for x in nums[:-1]:
            best = max(best, x)
            ret += best
        return ret
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
* [Greedy](/Collections/greedy.md#greedy)
