# Defuse the bomb

[Problem link](https://leetcode.com/problems/defuse-the-bomb/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n, psum = len(code), list(accumulate(code * 3))
        return [
            abs(psum[i + k - (k < 0)] - psum[i - (k < 0)])
            for i in range(n, 2 * n)
        ]
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Cyclic array](/Collections/array-scanning.md#cyclic-array)
