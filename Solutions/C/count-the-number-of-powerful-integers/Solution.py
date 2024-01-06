# https://leetcode.com/problems/count-the-number-of-powerful-integers/

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def digdp(m):
            l, ret = len(m), 0
            for i in range(l):
                ret += min(int(m[i]), limit + 1) * (limit + 1) ** (l - i - 1)
                if int(m[i]) > limit:
                    break
            else:
                ret += 1
            return ret

        def part(n):
            if n < int(s):
                return 0
            l = len(s)
            m = n // (10 ** l)
            if str(n)[-l:] < s:
                m -= 1
            return digdp(str(m)) if m >= 0 else 0

        return part(finish) - part(start - 1)
