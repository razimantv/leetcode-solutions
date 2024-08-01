# Count the number of special characters ii

[Problem link](https://leetcode.com/problems/count-the-number-of-special-characters-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-the-number-of-special-characters-ii/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first, last = {}, {}
        for i, c in enumerate(word):
            if c not in first:
                first[c] = i
            last[c] = i

        ret = 0
        for i in range(26):
            a, A = chr(ord('a') + i), chr(ord('A') + i)
            if a in first and A in first and last[a] < first[A]:
                ret += 1
        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Array scanning](/Collections/array-scanning.md#array-scanning)
