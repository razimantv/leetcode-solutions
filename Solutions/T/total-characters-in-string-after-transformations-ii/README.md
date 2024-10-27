# Total characters in string after transformations ii

[Problem link](https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

class Solution:
    def lengthAfterTransformations(
        self, s: str, t: int, nums: List[int]
    ) -> int:
        ctr, mod = Counter(s), 10 ** 9 + 7
        c0 = [[ctr[chr(ord('a') + i)]] for i in range(26)]

        M = [[0] * 26 for _ in range(26)]
        for i, x in enumerate(nums):
            for j in range(i + 1, i + x + 1):
                M[j % 26][i] = 1

        def mul(A, B):
            m, k, n = len(A), len(B), len(B[0])
            ret = [[0] * n for _ in range(m)]
            for p in range(m):
                for q in range(k):
                    for r in range(n):
                        ret[p][r] = (ret[p][r] + A[p][q] * B[q][r]) % mod
            return ret

        def mpow(A, n):
            ret = [[0] * len(A) for _ in range(len(A))]
            for i, row in enumerate(ret):
                row[i] = 1

            while n:
                if n & 1:
                    ret = mul(ret, A)
                A = mul(A, A)
                n >>= 1
            return ret

        Mp = mpow(M, t)
        Mpc0 = mul(Mp, c0)
        return sum(row[0] for row in Mpc0) % mod
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Graph-like state transitions](/Collections/dynamic-programming.md#graph-like-state-transitions)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Matrix exponentiation](/Collections/dynamic-programming.md#matrix-exponentiation)
