# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {c: 1 << i for i, c in enumerate('aeiou')}
        first, cur, ret = {0: -1}, 0, 0
        for i, c in enumerate(s):
            cur ^= vowels.get(c, 0)
            ret = max(ret, i - first.setdefault(cur, i))
        return ret
