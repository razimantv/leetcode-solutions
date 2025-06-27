# https://leetcode.com/problems/longest-subsequence-repeated-k-times/

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n, ctr = len(s), Counter(s)
        chars = sum(([c] * (x // k) for c, x in ctr.items()), start=[])
        if not chars:
            return ''
        L = len(chars)
        S = set(
            p[:i] for p in map(tuple, permutations(chars))
            for i in range(1, L + 1)
        )
        S = sorted(S, key=lambda x: (len(x), x), reverse=True)

        def work(t):
            i = 0
            for j in range(k):
                for c in t:
                    while i < n and s[i] != c:
                        i += 1
                    else:
                        if i == n:
                            return False
                        i += 1
            return True

        for poss in S:
            if work(poss):
                return ''.join(poss)
        return ''
