# https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        ctr = Counter(word2)
        r, miss, n, ret = 0, len(ctr), len(word1), 0
        for l in range(n):
            while miss and r < n:
                c = word1[r]
                ctr[c] -= 1
                if ctr[c] == 0:
                    miss -= 1
                r += 1
            if miss:
                break
            ret += n - r + 1
            c = word1[l]
            ctr[c] += 1
            if ctr[c] == 1:
                miss += 1
        return ret
