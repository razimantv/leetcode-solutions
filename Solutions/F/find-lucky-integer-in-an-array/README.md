# Find lucky integer in an array

[Problem link](https://leetcode.com/problems/find-lucky-integer-in-an-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        return max((k for k, v in Counter(arr).items() if k == v), default=-1)
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
