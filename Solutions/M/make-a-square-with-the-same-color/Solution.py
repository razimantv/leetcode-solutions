# https://leetcode.com/problems/make-a-square-with-the-same-color/

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                ctr = Counter([
                    grid[ii][jj] 
                    for ii in range(i, i + 2) for jj in range(j, j + 2)
                ])
                if max(ctr.values()) > 2:
                    return True
        return False
