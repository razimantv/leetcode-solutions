# Find center of star graph

[Problem link](https://leetcode.com/problems/find-center-of-star-graph/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        u, v = edges[0]
        return u if u in edges[1] else v
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory)
