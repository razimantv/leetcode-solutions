# Remove adjacent almost equal characters

[Problem link](https://leetcode.com/problems/remove-adjacent-almost-equal-characters/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n, i, ret = len(word), 1, 0
        while i < n:
            if abs(ord(word[i]) - ord(word[i-1])) < 2:
                ret += 1
                i += 1
            i += 1
        return ret
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
