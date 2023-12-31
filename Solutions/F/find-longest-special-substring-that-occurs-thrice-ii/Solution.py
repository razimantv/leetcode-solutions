# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

class Solution:
    def maximumLength(self, s: str) -> int:
        start, n = 0, len(s)
        cnt = defaultdict(lambda: defaultdict(int))
        for i in range(1, n + 1):
            if i == n or s[i] != s[i-1]:
                l, c = i - start, s[i-1]
                cnt[l][c] += 1
                cnt[l-1][c] += 2
                cnt[l-2][c] += 3
                start = i
        for l in range(n - 2, 0, -1):
            if max(cnt[l].values(), default=0) > 2:
                return l
        return -1
