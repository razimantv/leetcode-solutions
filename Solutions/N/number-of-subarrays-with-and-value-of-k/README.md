# Number of subarrays with and value of k

[Problem link](https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        last, ret = [-1] * 31, 0
        for i, x in enumerate(nums):
            for b in range(30):
                if not (x & (1 << b)):
                    last[b] = i
            todo = sorted(
                list([(pos, b) for b, pos in enumerate(last)]), reverse=True
            )
            mask = (1 << 30) - 1
            for j, (pos, b) in enumerate(todo):
                mask ^= (1 << b)
                if mask == k:
                    ret += pos - todo[j + 1][0]
        return ret
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with bit value](/Collections/array-scanning.md#location-of-previous-element-with-bit-value)
