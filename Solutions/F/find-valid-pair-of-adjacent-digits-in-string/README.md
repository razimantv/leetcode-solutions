# Find valid pair of adjacent digits in string

[Problem link](https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string

class Solution:
    def findValidPair(self, s: str) -> str:
        ctr = Counter(s)
        for x, y in pairwise(s):
            if x != y and ctr[x] == int(x) and ctr[y] == int(y):
                return x + y
        return ""
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Array scanning](/Collections/array-scanning.md#array-scanning)
