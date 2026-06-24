# Number of zigzag arrays ii

[Problem link](https://leetcode.com/problems/number-of-zigzag-arrays-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-zigzag-arrays-ii/

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        d, mod = r - l + 1, 10 ** 9 + 7
        M = [
            [(1 if i + j >= d else 0) for j in range(d)]
            for i in range(d)
        ]

        def mult(A, B):
            ret = [[0] * d for _ in range(d)]
            for i in range(d):
                for j in range(d):
                    for k in range(d):
                        ret[i][j] = (ret[i][j] + A[i][k] * B[k][j]) % mod
            return ret
            
        def matpow(M, k):
            if k == 1:
                return M
            elif k & 1:
                return mult(matpow(mult(M, M), k // 2), M)
            else: 
                return matpow(mult(M, M), k // 2)

        return sum(
            2 * x for row in matpow(M, n - 1) for x in row
        ) % mod
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Matrix exponentiation](/Collections/dynamic-programming.md#matrix-exponentiation)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
