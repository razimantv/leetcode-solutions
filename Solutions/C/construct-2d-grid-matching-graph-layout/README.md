# Construct 2d grid matching graph layout

[Problem link](https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

class Solution:
    def constructGridLayout(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        if n == 2:
            return [[0, 1]]

        deg, adj = [0] * n, [[] for _ in range(n)]
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            adj[u].append(v)
            adj[v].append(u)

        ctr = Counter(deg)
        mindeg, maxdeg = min(ctr), max(ctr)
        seen = [0] * n

        if mindeg == 1:
            start = [u for u in range(n) if deg[u] == 1][0]
            row = [start]
            seen[start] = 1
            for i in range(1, n):
                u = row[-1]
                v = [x for x in adj[u] if not seen[x]][0]
                row.append(v)
                seen[v] = 1
            return [row]
        elif maxdeg < 4:
            tl = [u for u in range(n) if deg[u] == 2][0]
            bl = [u for u in adj[tl] if deg[u] == 2][0]
            ret = [[tl], [bl]]
            seen[tl] = seen[bl] = 1
            while 2 * len(ret[0]) < n:
                t = [u for u in adj[ret[0][-1]] if not seen[u]][0]
                b = [u for u in adj[ret[1][-1]] if not seen[u]][0]
                ret[0].append(t)
                ret[1].append(b)
                seen[t] = seen[b] = 1
            return ret

        start = [u for u in range(n) if deg[u] == 2][0]
        row = [start]
        seen[start] = 1
        while (len(row) == 1 or deg[row[-1]] == 3):
            v = [u for u in adj[row[-1]] if deg[u] < 4 and not seen[u]][0]
            row.append(v)
            seen[v] = 1

        ret = [row]
        m = len(row)
        while len(ret) * len(ret[0]) < n:
            row = ret[-1]
            start = [u for u in adj[row[0]] if not seen[u]][0]
            newrow = [start]
            seen[start] = 1
            for i in range(1, m):
                v = [
                    u for u in adj[newrow[-1]]
                    if not seen[u] and u in adj[row[i]]
                ][0]
                newrow.append(v)
                seen[v] = 1
            ret.append(newrow)
        return ret
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Degree counting](/Collections/graph-theory.md#degree-counting)
* [Construction](/Collections/construction.md#construction)
