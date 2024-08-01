# Minimum number of moves to seat everyone

[Problem link](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(x - y) for x, y in zip(sorted(seats), sorted(students)))
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
