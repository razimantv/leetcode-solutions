# Reverse prefix of word

[Problem link](https://leetcode.com/problems/reverse-prefix-of-word/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, c in enumerate(word):
            if c == ch:
                return word[i::-1] + word[i + 1:]
        return word
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
