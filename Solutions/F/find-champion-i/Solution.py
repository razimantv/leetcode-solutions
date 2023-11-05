# https://leetcode.com/problems/find-champion-i/

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, row in enumerate(grid):
            if sum(row) == n-1:
                return i
        return -1
