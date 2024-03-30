# Shortest subarray with or at least k ii

[Problem link](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if not k:
            return 1
        n = len(nums)
        last, ret = {}, n + 1
        for i, x in enumerate(nums):
            for b in range(30):
                if x & (1 << b):
                    last[b] = i
            cur = 0
            for b, j in sorted(last.items(), key=lambda x: (-x[1], x[0])):
                cur |= 1 << b
                if cur >= k:
                    ret = min(ret, i-j+1)
                    break
        return ret if ret <= n else -1
```
## Tags

* [Array scanning](/README.md#Array_scanning) > [Location of previous element with same value](/README.md#Array_scanning-Location_of_previous_element_with_same_value)
* [Bitwise operation](/README.md#Bitwise_operation)
