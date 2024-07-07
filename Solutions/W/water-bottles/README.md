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

* [Mathematics](/README.md#Mathematics) > [Basic](/README.md#Mathematics-Basic)
