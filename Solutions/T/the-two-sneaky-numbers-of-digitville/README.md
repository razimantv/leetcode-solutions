# The two sneaky numbers of digitville

[Problem link](https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [x for x, y in Counter(nums).items() if y > 1]
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
