# https://leetcode.com/problems/process-string-with-special-operations-ii/

class Solution:
    def processStr(self, s: str, k: int) -> str:
        l, lengths = 0, []
        for c in s:
            if c == '*':
                l = max(l - 1, 0)
            elif c == '#':
                l *= 2
            elif c != '%':
                l += 1
            lengths. append (l)

        if lengths[-1] <= k:
            return '.'

        for l, c in zip(lengths[::-1], s[::-1]):
            if l - 1 == k and c not in '*#%':
                return c
            if c == '#':
                k %= l // 2
            elif c == '%':
                k = l - 1 - k
        return ''
