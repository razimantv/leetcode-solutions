# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ret = 0
        for i in range(m // 2):
            ip = m - 1 - i
            for j in range(n // 2):
                jp = n - 1 - j
                cur = grid[i][j] + grid[i][jp] + grid[ip][j] + grid[ip][jp]
                ret += min(cur, 4 - cur)
        
        zo, ones = False, 0
        if m & 1:
            mc = m // 2
            for j in range(n // 2):
                jp = n - 1 - j
                cur = grid[mc][j] + grid[mc][jp]
                ones = (ones + cur) & 3
                if cur == 1:
                    ret += 1
                    zo = True
        
        if n & 1:
            nc = n // 2
            for i in range(m // 2):
                ip = m - 1 - i
                cur = grid[i][nc] + grid[ip][nc]
                ones = (ones + cur) & 3
                if cur == 1:
                    ret += 1
                    zo = True
        
        if (m & 1) and (n & 1) and grid[m // 2][n // 2]:
            ret += 1
        
        if ones and not zo:
            ret += 2
        
        return ret
