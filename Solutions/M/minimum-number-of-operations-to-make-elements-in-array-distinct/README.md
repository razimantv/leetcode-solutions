# Minimum number of operations to make elements in array distinct

[Problem link](https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for x in nums[::-1]:
            if x in seen:
                break
            seen. add(x)
        remove = len(nums) - len(seen)
        return (remove + 2) // 3
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Right to left](/Collections/array-scanning.md#right-to-left)
* [Hashmap](/Collections/hashmap.md#hashmap)
