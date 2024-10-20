# https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n, ctr, r, ret = len(s), Counter(), 0, 0
        for l in range(n):
            while r < n and max(ctr.values(), default=0) < k:
                ctr[s[r]] += 1
                r += 1
            if max(ctr.values(), default=0) < k:
                break
            ret += n - r + 1
            ctr[s[l]] -= 1
        return ret
