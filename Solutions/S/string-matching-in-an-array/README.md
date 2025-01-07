# String matching in an array

[Problem link](https://leetcode.com/problems/string-matching-in-an-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/string-matching-in-an-array/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret, words = [], sorted(words, key=len)
        for i, x in enumerate(words):
            for y in words[i + 1:]:
                if y. find(x) != -1:
                    ret. append(x)
                    break
        return ret
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search)
