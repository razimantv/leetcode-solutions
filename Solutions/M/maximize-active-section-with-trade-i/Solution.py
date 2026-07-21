# https://leetcode.com/problems/maximize-active-section-with-trade-i/

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        prev, cur, ret = 0, 0, 0
        for c in s:
            if c == '0':
                cur += 1
                if prev:
                    ret = max(ret, cur + prev)
            else: 
                if cur:
                    prev, cur = cur, 0
        return ret + Counter(s)['1']
