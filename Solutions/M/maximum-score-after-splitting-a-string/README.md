# Maximum score after splitting a string

[Problem link](https://leetcode.com/problems/maximum-score-after-splitting-a-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        return max(
            Counter(s[:i])['0'] + Counter(s[i:])['1']
            for i in range(1, len(s))
        )
```
## Tags

* [Simple implementation](/README.md#Simple_implementation)
* [Suboptimal solution](/README.md#Suboptimal_solution)
