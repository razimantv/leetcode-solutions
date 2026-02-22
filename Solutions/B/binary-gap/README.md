# Binary gap

[Problem link](https://leetcode.com/problems/binary-gap/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/binary-gap/

class Solution:
    def binaryGap(self, n: int) -> int:
        return max(
            (
                y - x for x, y in pairwise(
                    i for i, c in enumerate(f'{n:b}') if c == '1'
                )
            ),
            default=0
        )
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
