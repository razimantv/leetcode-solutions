# Permutation difference between two strings

[Problem link](https://leetcode.com/problems/permutation-difference-between-two-strings/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/permutation-difference-between-two-strings/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos = {c: i for i, c in enumerate(s)}
        return sum(abs(i - pos[c]) for i, c in enumerate(t))
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
