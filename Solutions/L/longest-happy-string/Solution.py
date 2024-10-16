# https://leetcode.com/problems/longest-happy-string/

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        left, ret = [[a, 'a'], [b, 'b'], [c, 'c']], ''
        while True:
            left.sort(reverse=True)
            if not left[0][0]:
                break
            if ret[-2:] == left[0][1] * 2:
                if not left[1][0]:
                    break
                ret += left[1][1]
                left[1][0] -= 1
            else:
                ret += left[0][1]
                left[0][0] -= 1
        return ret
