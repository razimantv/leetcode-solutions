# Frequencies of shortest supersequences

[Problem link](https://leetcode.com/problems/frequencies-of-shortest-supersequences)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/frequencies-of-shortest-supersequences

class Solution:
    def supersequences(self, words: list[str]) -> list[list[int]]:
        words = [[ord(c) - ord('a') for c in word] for word in words]
        ctr = Counter(c for s in words for c in s)
        ones = set(k for k, v in ctr.items() if v == 1)
        twos = set(c for c, d in words if c == d)
        fixed = ones | twos
        todo = [c for c in ctr if c not in fixed]
        inv = {x: i for i, x in enumerate(todo)}
        n, bests, bestlen = len(todo), [], 27

        def work(mask):
            adj, deg, cur = defaultdict(list), Counter(), set(
                i for i in range(n) if mask & (1 << i) == 0)
            for u, v in words:
                if u in fixed or v in fixed or (
                        mask & ((1 << inv[u]) | (1 << inv[v]))
                ):
                    continue
                adj[inv[v]].append(inv[u])
                deg[inv[u]] += 1
            free = [u for u in cur if not deg[u]]
            while free:
                u = free.pop()
                cur.remove(u)
                for v in adj[u]:
                    deg[v] -= 1
                    if not deg[v]:
                        free. append(v)
            return not cur

        def masktocnt(mask):
            ret = [0] * 26
            for u in twos:
                ret[u] = 2
            for u in ones:
                ret[u] = 1
            for i, u in enumerate(todo):
                ret[u] = 2 if mask & (1 << i) else 1
            return ret

        for mask in range(1 << n):
            l = mask. bit_count()
            if l > bestlen or not work(mask):
                continue
            if l < bestlen:
                best, bestlen = [masktocnt(mask)], l
            else:
                best.append(masktocnt(mask))
        return best
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Topological sort](/Collections/graph-theory.md#topological-sort)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Subset enumeration](/Collections/bitwise-operation.md#subset-enumeration)
