# Water bottles

[Problem link](https://leetcode.com/problems/water-bottles/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, bottles: int, exchange: int) -> int:
        ret, empty = 0, 0
        while bottles:
            ret += bottles
            empty += bottles
            bottles = empty // exchange
            empty -= empty // exchange * exchange
        return ret
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Basic](/Collections/mathematics.md#basic)
