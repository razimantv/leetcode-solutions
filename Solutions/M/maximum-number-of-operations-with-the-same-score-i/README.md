# Maximum number of operations with the same score i

[Problem link](https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n, score = len(nums), nums[0] + nums[1]
        ret = 0
        for l in range(0, n - 1, 2):
            if nums[l] + nums[l + 1] == score:
                ret += 1
            else:
                break
        return ret
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
