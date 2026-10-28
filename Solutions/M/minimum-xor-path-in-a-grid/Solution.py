# https://leetcode.com/problems/minimum-xor-path-in-a-grid/


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        poss = [[set() for x in row] for row in grid]
        poss[0][0].add(grid[0][0])
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if i:
                    poss[i][j].update({x ^ y for y in poss[i - 1][j]})
                if j:
                    poss[i][j].update({x ^ y for y in poss[i][j - 1]})
        return min(poss[-1][-1])
