# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        o0, o1, n = 0, 0, len(s)
        for i, c in enumerate(s):
            if c == '0':
                if i % 2:
                    o1 += 1
                else:
                    o0 += 1
        return min(n - n // 2 - o0 + o1, o0 + n // 2 - o1)
