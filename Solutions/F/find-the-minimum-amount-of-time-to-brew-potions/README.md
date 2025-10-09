# Find the minimum amount of time to brew potions

[Problem link](https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        end = [0] * len(skill)
        for m in mana:
            psum = [0] + list(accumulate(m * x for x in skill))
            start = max(x - y for x, y in zip(end, psum))
            end = [x + start for x in psum[1:]]
        return end[-1]
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Array scanning](/Collections/array-scanning.md#array-scanning)
