# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rowsum = [sum(row) for row in mat]
        colsum = [sum(col) for col in zip(*mat)]
        return sum([
            1 for i in range(m) for j in range(n)
            if mat[i][j] == rowsum[i] == colsum[j] == 1
        ])
