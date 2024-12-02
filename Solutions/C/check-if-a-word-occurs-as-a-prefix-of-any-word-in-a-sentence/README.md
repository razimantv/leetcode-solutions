# Check if a word occurs as a prefix of any word in a sentence

[Problem link](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:
    def isPrefixOfWord(self, sentence: str, search: str) -> int:
        n = len(search)
        for i, word in enumerate(sentence.split()):
            if word[:n] == search:
                return i + 1
        return -1
```
## Tags

* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing)
* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Prefix/Suffix](/Collections/string.md#prefix-suffix)
