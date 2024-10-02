# Rank transform of an array

[Problem link](https://leetcode.com/problems/rank-transform-of-an-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {x: i + 1 for i, x in enumerate(sorted(list(set(arr))))}
        return [rank[x] for x in arr]
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
