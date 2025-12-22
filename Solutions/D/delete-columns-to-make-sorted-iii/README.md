# Delete columns to make sorted iii

[Problem link](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        dp = [0]
        for i in range(len(strs[0])):
            dp = [x + 1 for x in dp] + [i]
            for j in range(i):
                if all(s[i] >= s[j] for s in strs):
                    dp[-1] = min(dp[-1], dp[j + 1] - 1)
        return min(dp)
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
