# https://leetcode.com/problems/smallest-palindromic-rearrangement-i

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        pieces, end, ctr = [], '', Counter(s)
        for c in sorted(ctr):
            pieces.append(c * (ctr[c] // 2))
            if ctr[c] & 1:
                end = c
        ret = ''. join(pieces)
        return ret + end + ret[::-1]
