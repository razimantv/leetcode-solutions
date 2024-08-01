# Crawler log folder

[Problem link](https://leetcode.com/problems/crawler-log-folder/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for folder in logs:
            if folder[1] == '.':
                depth = max(depth - 1, 0)
            elif folder[0] != '.':
                depth += 1
        return depth
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
