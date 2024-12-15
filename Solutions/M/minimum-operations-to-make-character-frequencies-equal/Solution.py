# https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal

class Solution:
    def makeStringGood(self, s: str) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        def fix(a, b, c):
            if b >= c:
                return b - c + min(a, abs(c - a))
            if a >= c:
                delta = min(a - c, c - b)
                a, b = a - delta, b + delta
                return delta + a - b
            delta = min(a, c - b)
            a, b = a - delta, b + delta
            return delta + a + c - b

        def work(c):
            dp = [math.inf] * 26
            for i in range(26):
                dp[i] = min(cnt[i], abs(cnt[i] - c)) + (dp[i - 1] if i else 0)
                if i > 0:
                    dp[i] = min(
                        dp[i],
                        fix(cnt[i - 1], cnt[i], c) + (
                            dp[i - 2] if i > 1 else 0
                        )
                    )
            return dp[-1]

        return min(work(c) for c in range(max(cnt) + 1))
