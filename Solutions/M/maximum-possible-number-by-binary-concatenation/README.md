# Maximum possible number by binary concatenation

[Problem link](https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        ret = ""
        for perm in permutations(nums):
            ret = max(ret, ''.join(f"{x:b}" for x in perm))

        return int(ret, 2)
```
## Tags

* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Combinatorial](/Collections/brute-force-enumeration.md#combinatorial)
