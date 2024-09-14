# Find indices of stable mountains

[Problem link](https://leetcode.com/problems/find-indices-of-stable-mountains/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-indices-of-stable-mountains/

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [
            i + 1 for i, (x, y) in enumerate(pairwise(height))
            if x > threshold
        ]
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
