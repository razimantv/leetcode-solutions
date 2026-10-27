# Create grid with exactly one path

[Problem link](https://leetcode.com/problems/create-grid-with-exactly-one-path/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/create-grid-with-exactly-one-path/


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return [
            "".join("." if i == 0 or j == n - 1 else "#" for j in range(n))
            for i in range(m)
        ]
```
## Tags

* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
