# Count the number of houses at a certain distance i

[Problem link](https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x, y = min(x-1, y-1), max(x-1, y-1)
        if y - x < 2:
            return [2 * i for i in range(n-1, -1, -1)]

        pref = [0] * n
        d1n = x + n - y
        for lim in [x, n - 1 - y]:
            for i in range(lim):
                pref[0] += 2
                pref[i] -= 1
                pref[d1n - i] -= 1

        c = y - x + 1
        pref[0] += 2 * c
        pref[(c - 1) // 2] -= c
        pref[c // 2] -= c

        for i in range(x, y + 1):
            inc = 1 if i in [x, y] else 2
            if i - x < y - i + 1:
                # min: i - x + 1, max: i
                pref[i - x] += inc
                pref[i] -= inc
            else:
                # min: y - i + 2, max: y - i + 1 + x
                pref[y - i + 1] += inc
                pref[x + y - i + 1] -= inc

            if i - x + 1 < y - i:
                # min: i - x + 2, max: n - 1 - y + 1 + i - x
                pref[i - x + 1] += inc
                pref[n - y + i - x] -= inc
            else:
                # min: y + 1 - i, max: n - i - 1
                pref[y - i] += inc
                pref[n - i - 1] -= inc

        return accumulate(pref)
# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [For range updates](/Collections/prefix.md#for-range-updates)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Single cycle graphs](/Collections/graph-theory.md#single-cycle-graphs)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
