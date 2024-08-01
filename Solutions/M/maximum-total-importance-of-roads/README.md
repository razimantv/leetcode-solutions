# Maximum total importance of roads

[Problem link](https://leetcode.com/problems/maximum-total-importance-of-roads/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = sorted(
            Counter((u for road in roads for u in road)). values(),
            reverse=True
        )
        return sum(x * y for x, y in zip(degrees, range(n, 0, -1)))
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Degree counting](/Collections/graph-theory.md#degree-counting)
* [Greedy](/Collections/greedy.md#greedy)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
