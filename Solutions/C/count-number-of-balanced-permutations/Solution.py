# https://leetcode.com/problems/count-number-of-balanced-permutations/

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10 ** 9 + 7

        @cache
        def ncr(n, r):
            if r == 0 or r == n:
                return 1
            return (ncr(n - 1, r) + ncr(n - 1, r - 1)) % mod

        ctr = Counter([int(d) for d in num])
        n = len(num)
        even, odd = n // 2, (n + 1) // 2

        @cache
        def dp(even, odd, d, target):
            if d == 10:
                return target == 0
            nd = ctr[d]
            ret = 0
            for ne in range(max(0, nd - odd), min(nd, even) + 1):
                no = nd - ne
                ret = (
                    ret +
                    (
                        ncr(even, ne) * ncr(odd, no) *
                        dp(even - ne, odd - no, d + 1, target + (no - ne) * d)
                    )
                ) % mod

            return ret

        return dp(even, odd, 0, 0)
