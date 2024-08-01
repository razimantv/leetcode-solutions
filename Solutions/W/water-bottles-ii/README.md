# Water bottles ii

[Problem link](https://leetcode.com/problems/water-bottles-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/water-bottles-ii/

class Solution:
    def maxBottlesDrunk(self, bottles: int, exchange: int) -> int:
        ret = bottles
        while bottles >= exchange:
            ret += 1
            bottles -= exchange - 1
            exchange += 1
        return ret
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
