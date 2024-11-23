# https://leetcode.com/problems/shift-distance-between-two-strings

class Solution:
    def shiftDistance(
        self, s: str, t: str, nextCost: List[int], previousCost: List[int]
    ) -> int:
        psum1 = [0] + list(accumulate(nextCost))
        psum2 = [0] + list(accumulate(previousCost))
        ret = 0
        for c, d in zip(s, t):
            c, d = ord(c) - ord('a'), ord(d) - ord('a')
            if d > c:
                ret += min(
                    psum1[d] - psum1[c],
                    psum2[c + 1] + psum2[-1] - psum2[d + 1]
                )
            else:
                ret += min(
                    psum1[-1] - psum1[c] + psum1[d],
                    psum2[c + 1] - psum2[d + 1]
                )
        return ret
