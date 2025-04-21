# Count the hidden sequences

[Problem link](https://leetcode.com/problems/count-the-hidden-sequences/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-the-hidden-sequences/

class Solution:
    def numberOfArrays(
        self, differences: list[int], lower: int, upper: int
    ) -> int:
        ar = [0] + list(accumulate(differences))
        return max(0, upper - lower - (max(ar) - min(ar)) + 1)
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
