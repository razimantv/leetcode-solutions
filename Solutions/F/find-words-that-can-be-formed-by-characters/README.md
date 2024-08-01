# Find words that can be formed by characters

[Problem link](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)

        def good(word):
            for c, x in Counter(word).items():
                if c not in cnt or x > cnt[c]:
                    return False
            return True

        return sum(len(word) for word in words if good(word))
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
