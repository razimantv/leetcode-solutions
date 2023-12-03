# https://leetcode.com/problems/count-the-number-of-infection-sequences/

class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        MOD = 10 ** 9 + 7
        fac, pow2 = [-1] * n, [-1] * n
        fac[0], pow2[0] = 1, 1
        facmax, pow2max = 0, 0

        def inv(a, b):
            r0, r1, s0, s1, t0, t1 = a, b, 1, 0, 0, 1
            while r1:
                q = r0 // r1
                r0, r1, s0, s1, t0, t1 = (
                    r1, r0 - q * r1,
                    s1, s0 - q * s1,
                    t1, t0 - q * t1
                )

            s0 %= b
            if s0 < 0:
                s0 += b
            return s0

        def ncr(n, r):
            nonlocal facmax
            if fac[n] == -1:
                while facmax < n:
                    facmax += 1
                    fac[facmax] = (fac[facmax-1] * facmax) % MOD

            return (fac[n] * inv((fac[r] * fac[n-r]) % MOD, MOD)) % MOD

        def p2(n):
            nonlocal pow2max
            if pow2[n] == -1:
                while pow2max < n:
                    pow2max += 1
                    pow2[pow2max] = (pow2[pow2max - 1] * 2) % MOD

            return pow2[n]

        ret = 1
        used = 0
        for i, j in pairwise(sick):
            space = j - i - 1
            if not space:
                continue
            ret = (ret * ncr(used + space, space) * p2(space - 1)) % MOD
            used += space

        for space in [sick[0], n-1-sick[-1]]:
            if space:
                ret = (ret * ncr(used + space, space)) % MOD
                used += space

        return ret
