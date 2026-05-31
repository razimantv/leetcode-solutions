# Destroying asteroids

[Problem link](https://leetcode.com/problems/destroying-asteroids/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/destroying-asteroids/

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        for x in sorted(asteroids):
            if x > mass: 
                return False
            mass += x
        return True
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
