# https://leetcode.com/problems/relative-ranks/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rankscores = sorted([(-x, i) for i, x in enumerate(score)])
        for r, (x, i) in enumerate(rankscores):
            score[i] = str(r + 1) if r > 2 else [
                "Gold", "Silver", "Bronze"
            ][r] + " Medal"
        return score
