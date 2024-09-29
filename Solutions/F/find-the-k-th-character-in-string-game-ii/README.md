# Find the k th character in string game ii

[Problem link](https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n, L = 0, 1
        while L < k:
            n, L = n + 1, L << 1
        k -= 1

        ret = 0
        while n:
            n, L = n - 1, L >> 1
            if operations[n] and k >= L:
                ret += 1
            k %= L
        return chr(ord('a') + ret % 26)
```
## Tags

* [Construction](/Collections/construction.md#construction)
* [Time reversed simulation](/Collections/time-reversed-simulation.md#time-reversed-simulation)
