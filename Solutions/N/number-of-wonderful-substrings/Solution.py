# https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt, pref, ret = defaultdict(int), 0, 0
        for c in word:
            cnt[pref] += 1
            pref ^= (1 << (ord(c) - ord('a')))
            ret += cnt[pref] + sum(cnt[pref ^ (1 << i)] for i in range(10))
        return ret
