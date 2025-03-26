# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        grid = sorted([v for row in grid for v in row])
        if any((b - a) % x for a, b in pairwise(grid)):
            return -1
        target = grid[len(grid) // 2]
        return sum(abs(v - target) for v in grid) // x
