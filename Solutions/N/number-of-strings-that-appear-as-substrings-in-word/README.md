# Number of strings that appear as substrings in word

[Problem link](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        return sum((1 for p in patterns if p in word))
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
