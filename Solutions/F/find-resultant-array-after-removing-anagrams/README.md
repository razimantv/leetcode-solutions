# Find resultant array after removing anagrams

[Problem link](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        ret = []
        for word in words:
            if not ret or sorted(ret[-1]) != sorted(word):
                ret. append(word)
        return ret
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
* [String](/Collections/string.md#string) > [Anagrams](/Collections/string.md#anagrams)
