# Lexicographical numbers

[Problem link](https://leetcode.com/problems/lexicographical-numbers/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/lexicographical-numbers/

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []

        def work(x):
            for y in range(max(1, 10 * x), min(n, 10 * x + 9) + 1):
                ret.append(y)
                work(y)
        work(0)
        return ret
```
### Solution_naive.py
```py
# https://leetcode.com/problems/lexicographical-numbers/

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(list(range(1, n + 1)), key=str)
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking)
