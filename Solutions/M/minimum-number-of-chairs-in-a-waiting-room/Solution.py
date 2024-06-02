# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

class Solution:
    def minimumChairs(self, s: str) -> int:
        cur, ret = 0, 0
        for c in s:
            cur += 1 if c == 'E' else -1
            ret = max(ret, cur)
        return ret
