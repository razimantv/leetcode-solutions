# https://leetcode.com/problems/zigzag-grid-traversal-with-skip

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ret = []
        for x in range(0, m * n, 2):
            i, j = x // n, x % n
            if i & 1:
                j = n - 1 - j
            ret.append(grid[i][j])
        return ret
