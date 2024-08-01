# Find minimum operations to make all elements divisible by three

[Problem link](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for x in nums if x % 3)
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Basic](/Collections/mathematics.md#basic)
