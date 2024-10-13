# Count the number of winning sequences

[Problem link](https://leetcode.com/problems/count-the-number-of-winning-sequences/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-the-number-of-winning-sequences/

class Solution:
    def countWinningSequences(self, s: str) -> int:
        types = 'FWE'
        order = {c: i for i, c in enumerate(types)}
        mod = 10 ** 9 + 7

        def score(c):
            oc = order[c]
            return [(i, types[(oc + i + 3) % 3]) for i in range(-1, 2)]

        dp = {sc: 1 for sc in score(s[0])}
        for c in s[1:]:
            scores = score(c)
            newdp = defaultdict(int)
            for (prevscore, lastchar), cnt in dp.items():
                for add, c in scores:
                    if c != lastchar:
                        next = (prevscore + add, c)
                        newdp[next] = (newdp[next] + cnt) % mod
            dp = newdp
        return sum(x for (sc, c), x in dp.items() if sc > 0) % mod
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Graph-like state transitions](/Collections/dynamic-programming.md#graph-like-state-transitions)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Two player games](/Collections/two-player-games.md#two-player-games)
