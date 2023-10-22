# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        n = len(jobs)
        if n < d:
            return -1

        dp = [0] * n
        for i in range(n):
            dp[i] = max(jobs[i], dp[i-1] if i else 0)

        inf = 1 << 30
        for k in range(1, d):
            newdp = [inf] * n
            mon = []
            for j in range(n):
                x = jobs[j]
                y = dp[j-1] if j else inf
                while mon:
                    dpi, vi, best = mon[-1]
                    if vi <= x:
                        y = min(y, dpi)
                        mon.pop()
                    else:
                        break
                best = mon[-1][2] if mon else inf
                best = min(best, x+y)
                mon.append((y, x, best))
                newdp[j] = best
            dp = newdp
        return dp[-1]
