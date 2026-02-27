# Minimum operations to equalize binary string

[Problem link](https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        z, n = Counter(s)['0'], len(s)

        dist, cur, next = [-1] * (n + 4), [z], []
        dist[z] = 0
        todo = [SortedList(list(range(i, n + 3, 2))) for i in (0, 1)]
        todo[z & 1].remove(z)

        while cur:
            for z in cur:
                par = (z + k) & 1
                zmin = z + k - 2 * min(k, z)
                zmax = z + k - 2 * max(0, k + z - n)
                while (
                    znext := todo[par][idx := todo[par].bisect_left(zmin)]
                ) <= zmax:
                    dist[znext] = dist[z] + 1
                    todo[par].pop(idx)
                    next.append(znext)

            cur, next = next, []

        return dist[0]
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Parity](/Collections/mathematics.md#parity)
* [Binary search](/Collections/binary-search.md#binary-search) > [Python SortedList](/Collections/binary-search.md#python-sortedlist)
