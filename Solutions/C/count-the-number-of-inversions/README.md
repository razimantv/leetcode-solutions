# Count the number of inversions

[Problem link](https://leetcode.com/problems/count-the-number-of-inversions/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-the-number-of-inversions/

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        requirements.sort()
        old, ret = (-1, 0), 1
        for pos, cnt in requirements:
            if cnt < old[1]:
                return 0
            todo = cnt - old[1]
            dp = [1] + [0] * todo
            mod = 10 ** 9 + 7
            for p in range(old[0], pos):
                dpsum = list(accumulate(dp))
                dp = [
                    (
                        dpsum[i] + mod
                        - (dpsum[i - p - 2] if i >= p + 2 else 0) % mod
                    ) % mod
                    for i in range(todo + 1)
                ]
            ret = (ret * dp[-1]) % mod
            old = (pos, cnt)
        return ret
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
