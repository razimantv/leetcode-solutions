# https://leetcode.com/problems/find-the-winning-player-in-coin-game/

class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        return 'Alice' if min(x, y // 4) & 1 else 'Bob'
