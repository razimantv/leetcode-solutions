# Minimize length of array using operations

[Problem link](https://leetcode.com/problems/minimize-length-of-array-using-operations/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimize-length-of-array-using-operations/

class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        xmin = min(nums)
        if ctr[xmin] == 1:
            return 1
        for x in nums:
            if x % xmin:
                return 1
        return (ctr[xmin] + 1) // 2
```
## Tags

* [Hashmap](/README.md#Hashmap) > [Counter](/README.md#Hashmap-Counter)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
