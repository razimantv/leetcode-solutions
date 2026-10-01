# Minimum costs using the train line

[Problem link](https://leetcode.com/problems/minimum-costs-using-the-train-line/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-costs-using-the-train-line/

class Solution:
    def minimumCosts(
        self, regular: list[int], express: list[int], c: int
    ) -> list[int]:
        a, b, ret = 0, c, []
        for c1, c2 in zip(regular, express):
            a, b = min(a + c1, b + c2), min(a + c1 + c, b + c2)
            ret.append(min(a, b))
        return ret
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
