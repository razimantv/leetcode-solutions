# Destination city

[Problem link](https://leetcode.com/problems/destination-city/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pair = {u: v for u, v in paths}
        u = paths[0][0]
        while u in pair:
            u = pair[u]
        return u
```
## Tags

* [Graph theory](/README.md#Graph_theory) > [Single outdegree graphs](/README.md#Graph_theory-Single_outdegree_graphs)
