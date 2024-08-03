# https://leetcode.com/problems/find-the-number-of-winning-players/

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        return len([
            i for i in range(n)
            if max(
                Counter(y for x, y in pick if x == i).values(), default=0
            ) > i
        ])
