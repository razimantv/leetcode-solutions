# Find the k th character in string game i

[Problem link](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            word += ''.join(
                chr(ord('a') + (ord(c) - ord('a') + 1) % 26) for c in word
            )
        return word[k - 1]
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
