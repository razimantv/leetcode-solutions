# https://leetcode.com/problems/ip-to-cidr/

class Solution:
    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        def dots2n(dots):
            return sum(
                (1 << (8 * (3 - i))) * int(x)
                for i, x in enumerate(dots. split('.'))
            )

        def n2dots(n):
            parts = []
            for i in range(4):
                parts. append(n & 255)
                n >>= 8
            return '.'. join(map(str, parts[::-1]))

        l = dots2n(ip)
        r = l + n - 1
        ret = []

        def work(n, b, L, R, l, r):
            if (L, R) == (l, r):
                ret.append(n2dots(n) + '/' + str(b))
                return
            M = (L + R) >> 1
            if l <= M:
                work(n, b + 1, L, M, l, min(M, r))
            if r > M:
                work(n ^ (1 << (31 - b)), b + 1, M + 1, R, max(l, M + 1), r)

        work(0, 0, 0, (1 << 32) - 1, l, r)
        return ret
