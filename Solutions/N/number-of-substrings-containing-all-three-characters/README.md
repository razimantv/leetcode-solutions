# Number of substrings containing all three characters

[Problem link](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last, ret = {c: -1 for c in 'abc'}, 0
        for i, c in enumerate(s):
            last[c] = i
            ret += min(last. values()) + 1
        return ret
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with same value](/Collections/array-scanning.md#location-of-previous-element-with-same-value)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
