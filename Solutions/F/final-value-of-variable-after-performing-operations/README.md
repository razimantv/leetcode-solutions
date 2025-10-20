# Final value of variable after performing operations

[Problem link](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum(1 if s[1] == '+' else -1 for s in operations)
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
