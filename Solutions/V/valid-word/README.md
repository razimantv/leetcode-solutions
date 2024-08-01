# Valid word

[Problem link](https://leetcode.com/problems/valid-word/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/valid-word/

class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'aeiouAEIOU'

        def goodchar(c):
            return 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9'

        def isvowel(c):
            return c in vowels

        def isconsonant(c):
            return ('a' <= c <= 'z' or 'A' <= c <= 'Z') and not isvowel(c)

        hasvowel, hasconsonant = False, False
        if len(word) < 3:
            return False

        for c in word:
            if not goodchar(c):
                return False
            elif isvowel(c):
                hasvowel = True
            elif isconsonant(c):
                hasconsonant = True

        return hasvowel and hasconsonant
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
