# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cnt = {'A': 0, 'B': 0}
        for i, c in enumerate(colors[1:-1]):
            if colors[i] == c and colors[i+2] == c:
                cnt[c] += 1
        return cnt['A'] > cnt['B']
