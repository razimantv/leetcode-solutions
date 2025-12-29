# Pyramid transition matrix

[Problem link](https://leetcode.com/problems/pyramid-transition-matrix/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/pyramid-transition-matrix/

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        amap = defaultdict(list)
        for a, b, c in allowed:
            amap[(a, b)]. append(c)

        n = len(bottom)
        state = [[''] * i for i in range(1, n)] + [list(bottom)]

        def work(i, j):
            poss = amap[tuple(state[i+1][j:j+2])]
            if not (i + j) and poss:
                return True
            ii, jj = (i, j + 1) if j < i else (i - 1, 0)
            for state[i][j] in poss:
                if work(ii, jj):
                    return True
            return False

        return work(n - 2, 0)
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking)
