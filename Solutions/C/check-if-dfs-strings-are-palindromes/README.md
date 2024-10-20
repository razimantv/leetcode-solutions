# Check if dfs strings are palindromes

[Problem link](https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        adj, ret = [[] for _ in range(n)], [True] * n
        for i, par in enumerate(parent[1:]):
            adj[par].append(i + 1)

        p1, mod1 = 43, 109357193
        p2, mod2 = 37, 103972513
        ppow1, ppow2 = [1], [1]
        for i in range(n):
            ppow1.append((ppow1[-1] * p1) % mod1)
            ppow2.append((ppow2[-1] * p2) % mod2)

        s = [ord(c) - ord('a') + 1 for c in s]

        def dfs(u, p, mod, ppow):
            n, front, back = 0, 0, 0
            for v in adj[u]:
                nc, fc, bc = dfs(v, p, mod, ppow)
                front = (front * ppow[nc] + fc) % mod
                back = (bc * ppow[n] + back) % mod
                n += nc

            front = (front * p + s[u]) % mod
            back = (s[u] * ppow[n] + back) % mod
            n += 1

            if front != back:
                ret[u] = False
            return n, front, back

        dfs(0, p1, mod1, ppow1)
        dfs(0, p2, mod2, ppow2)
        return ret
```
## Tags

* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Hashing](/Collections/string.md#hashing) > [Double hashing](/Collections/string.md#double-hashing)
* [Palindrome](/Collections/palindrome.md#palindrome) > [Hashing](/Collections/palindrome.md#hashing)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees) > [DP over children](/Collections/dynamic-programming.md#dp-over-children)
