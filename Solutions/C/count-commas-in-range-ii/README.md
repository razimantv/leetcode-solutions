# Count commas in range ii

[Problem link](https://leetcode.com/problems/count-commas-in-range-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-commas-in-range-ii/

class Solution:
    def countCommas(self, n: int) -> int:
        start, end, L, ret = 1000, 9999, 3, 0
        while start <= n:
            ret += (min(n, end) + 1 - start) * (L // 3)
            start, end, L = end + 1, end * 10 + 9, L + 1
        return ret
```
## Tags

* [Two pointers](/Collections/two-pointers.md#two-pointers)
