# https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        ret, coins, n = 0, sorted(coins), len(coins) 
        
        l, cur = 0, 0
        for r in range(n):
            cur += coins[r][2] * (coins[r][1] - coins[r][0] + 1)
            while l < n and coins[r][1] - coins[l][0] >= k:
                cur -= coins[l][2] * (coins[l][1] - coins[l][0] + 1)
                l += 1
            add = 0 if l == 0 or coins[r][1] - coins[l - 1][1] >= k else (
                coins[l - 1][2] * (coins[l - 1][1] - coins[r][1] + k)
            )
            ret = max(ret, cur + add)
        
        r, cur = n - 1, 0
        for l in range(n - 1, -1, -1):
            cur += coins[l][2] * (coins[l][1] - coins[l][0] + 1)
            while r >= 0 and coins[r][1] - coins[l][0] >= k:
                cur -= coins[r][2] * (coins[r][1] - coins[r][0] + 1)
                r -= 1
            add = 0 if r == n - 1 or coins[r + 1][0] - coins[l][0] >= k else (
                coins[r + 1][2] * (coins[l][0] - coins[r + 1][0] + k)
            )
            ret = max(ret, cur + add)
            
        return ret
