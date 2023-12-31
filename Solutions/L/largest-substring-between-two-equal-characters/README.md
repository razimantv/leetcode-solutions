# Largest substring between two equal characters

[Problem link](https://leetcode.com/problems/largest-substring-between-two-equal-characters/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ret, seen = -1, {}
        for i, c in enumerate(s):
            if c in seen:
                ret = max(ret, i - seen[c] - 1)
            else:
                seen[c] = i
        return ret
```
## Tags

* [Array scanning](/README.md#Array_scanning) > [Location of previous element with same value](/README.md#Array_scanning-Location_of_previous_element_with_same_value)
