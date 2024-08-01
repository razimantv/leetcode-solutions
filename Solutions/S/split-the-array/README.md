# Split the array

[Problem link](https://leetcode.com/problems/split-the-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/split-the-array/

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return max(Counter(nums).values()) <= 2
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
