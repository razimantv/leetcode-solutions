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

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
