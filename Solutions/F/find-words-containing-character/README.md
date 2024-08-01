# Find words containing character

[Problem link](https://leetcode.com/problems/find-words-containing-character/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-words-containing-character/

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
