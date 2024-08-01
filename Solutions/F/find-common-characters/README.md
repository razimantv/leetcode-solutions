# Find common characters

[Problem link](https://leetcode.com/problems/find-common-characters/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ctr = reduce(iand, [Counter(word) for word in words])
        return [c for c, x in ctr. items() for i in range(x)]
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
