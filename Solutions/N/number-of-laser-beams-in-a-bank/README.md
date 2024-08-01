# Number of laser beams in a bank

[Problem link](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        counts = [cnt for row in bank if (cnt := row.count('1'))]
        return sum(c1 * c2 for c1, c2 in pairwise(counts))
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
