# https://leetcode.com/problems/count-number-of-teams/

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        cnt = [[[0] * n for _ in [0, 1]] for _ in [0, 1]]
        for i in range(n):
            for j in range(i):
                cnt[0][rating[i] < rating[j]][i] += 1
                cnt[1][rating[i] > rating[j]][j] += 1

        ret = 0
        for i in range(n):
            ret += cnt[0][0][i] * cnt[1][1][i] + cnt[0][1][i] * cnt[1][0][i]
        return ret
