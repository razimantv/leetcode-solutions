# Construct product matrix

[Problem link](https://leetcode.com/problems/construct-product-matrix/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/construct-product-matrix/

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        tl = [[1]*(n+2) for _ in range(m+2)]
        tr = [[1]*(n+2) for _ in range(m+2)]
        bl = [[1]*(n+2) for _ in range(m+2)]
        br = [[1]*(n+2) for _ in range(m+2)]

        MOD = 12345
        for i in range(m):
            l, r = 1, 1
            for j in range(n):
                l = (l * grid[i][j]) % MOD
                tl[i+1][j+1] = (tl[i][j+1] * l) % MOD
            for j in range(n-1, -1, -1):
                r = (r * grid[i][j]) % MOD
                tr[i+1][j+1] = (tr[i][j+1] * r) % MOD

        for i in range(m-1, -1, -1):
            l, r = 1, 1
            for j in range(n):
                l = (l * grid[i][j]) % MOD
                bl[i+1][j+1] = (bl[i+2][j+1] * l) % MOD
            for j in range(n-1, -1, -1):
                r = (r * grid[i][j]) % MOD
                br[i+1][j+1] = (br[i+2][j+1] * r) % MOD

        ret = [[1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ret[i][j] = (
                    tl[i+1][j] * tr[i][j+1] * bl[i+2][j+1] * br[i+1][j+2]
                ) % MOD
        return ret
```
## Tags

* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum) > [2D](/README.md#Prefix-Sum-2D)
* [Matrix](/README.md#Matrix) > [Prefix](/README.md#Matrix-Prefix)
* [Array scanning](/README.md#Array_scanning) > [From both ends of array](/README.md#Array_scanning-From_both_ends_of_array) > [Element exclusion](/README.md#Array_scanning-From_both_ends_of_array-Element_exclusion)
