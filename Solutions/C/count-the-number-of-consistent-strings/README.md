# Count the number of consistent strings

[Problem link](https://leetcode.com/problems/count-the-number-of-consistent-strings/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return len([word for word in words if all(c in allowed for c in word)])
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
