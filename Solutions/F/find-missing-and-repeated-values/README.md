# Find missing and repeated values

[Problem link](https://leetcode.com/problems/find-missing-and-repeated-values/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-missing-and-repeated-values/

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nsq = n * n
        seen, missing = {}, (nsq * (nsq + 1)) // 2
        for row in grid:
            for x in row:
                if x in seen:
                    double = x
                else:
                    missing -= x
                    seen[x] = 1
        return [double, missing]
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Unique/duplicate element finding with bizarro algorithms](/Collections/unique-duplicate-element-finding-with-bizarro-algorithms.md#unique-duplicate-element-finding-with-bizarro-algorithms)
