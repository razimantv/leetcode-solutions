# Minimum length of string after deleting similar ends

[Problem link](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            while l <= r and s[l] == s[r]:
                l += 1
            while l <= r and s[l - 1] == s[r]:
                r -= 1

        return r - l + 1
```
## Tags

* [Two pointers](/Collections/two-pointers.md#two-pointers)
