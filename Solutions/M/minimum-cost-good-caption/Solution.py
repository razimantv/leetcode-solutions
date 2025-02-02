# https://leetcode.com/problems/minimum-cost-good-caption

class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        oa = ord('a')
        n, s = len(caption), [ord(c) - oa for c in caption]
        if n < 3:
            return ''
        caption += '$'
        dp = [(math.inf, '', '', n)] * n + [(0, '', '', n)]
        for i in range(n - 3, -1, -1):
            chars = set(caption[i:i + 5])
            for j in range(i + 2, min(i + 5, n)):
                for cc in chars:
                    ci = ord(cc) - oa
                    newcost = sum(
                        abs(ci - c) for c in s[i: j + 1]
                    ) + dp[j + 1][0]
                    if dp[j + 1][1] == cc:
                        newnext, newpos = dp[j + 1][2:]
                    else:
                        newnext, newpos = dp[j + 1][1], j + 1
                    if (newcost, cc) < dp[i][:2]:
                        dp[i] = newcost, cc, newnext, newpos
                    elif (newcost, cc) == dp[i][:2]:
                        conflict = min(newpos, dp[i][3])
                        c1 = dp[i][1] if conflict < dp[i][3] else dp[i][2]
                        c2 = cc if conflict < newpos else newnext
                        if c2 < c1:
                            dp[i] = newcost, cc, newnext, newpos
        i, ret = 0, ''
        while i < n:
            ret += dp[i][1] * (dp[i][3] - i)
            i = dp[i][3]
        return ret
