# Matrix similarity after cyclic shifts

[Problem link](https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        def good(ar, k):
            n = len(ar)
            k %= n
            cp = ar[k:] + ar[:k]
            return ar == cp

        for row in mat:
            if not good(row, k):
                return False
        return True
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
