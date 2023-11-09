# Count number of homogenous substrings

[Problem link](https://leetcode.com/problems/count-number-of-homogenous-substrings/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-number-of-homogenous-substrings/

class Solution:
    def countHomogenous(self, s: str) -> int:
        ret, cur = 1, 1
        for i in range(1, len(s)):
            cur = (cur + 1) if s[i] == s[i-1] else 1
            ret += cur
        return ret % (10**9 + 7)
```
## Tags

* [Array scanning](/README.md#Array_scanning) > [Contiguous region](/README.md#Array_scanning-Contiguous_region)
* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
