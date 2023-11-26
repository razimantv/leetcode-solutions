# Largest submatrix with rearrangements

[Problem link](https://leetcode.com/problems/largest-submatrix-with-rearrangements/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/

class Solution:
    def largestSubmatrix(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        for i in range(1, m):
            for j in range(n):
                if mat[i][j]:
                    mat[i][j] += mat[i-1][j]

        best = 0
        for row in mat:
            for i, x in enumerate(sorted(row)):
                best = max(best, x * (n-i))
        return best
```
## Tags

* [Array scanning](/README.md#Array_scanning) > [Contiguous region](/README.md#Array_scanning-Contiguous_region)
* [Sorting](/README.md#Sorting)
* [Matrix](/README.md#Matrix)
