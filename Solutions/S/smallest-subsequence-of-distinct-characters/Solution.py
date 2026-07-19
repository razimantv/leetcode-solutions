# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        cnt, mono, seen = Counter(s), [], {}
        for c in s:
            cnt[c] -= 1
            if c in seen:
                continue
            while mono and mono[-1] > c and cnt[mono[-1]]:
                seen.pop(mono[-1])
                mono.pop()
            mono.append(c)
            seen[c] = 1
        return ''. join(mono)
