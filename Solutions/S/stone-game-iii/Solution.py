# https://leetcode.com/problems/stone-game-iii/

class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        n = len(stones)
        dp = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            dp[i] = max(
                sum(stones[i:j+1]) - dp[j+1]
                for j in range(i, min(i + 3, n))
            )
        return 'Alice' if dp[0] > 0 else 'Bob' if dp[0] < 0 else 'Tie'
