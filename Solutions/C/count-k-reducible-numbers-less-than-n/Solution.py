# https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        n = len(s)
        steps, good = [0] * (n + 1), [1]
        for i in range(2, n + 1):
            steps[i] = steps[i.bit_count()] + 1
            if steps[i] < k:
                good.append(i)

        @cache
        def ncr(n, r):
            if r == 0:
                return 1
            elif r > n:
                return 0
            return (ncr(n - 1, r) + ncr(n - 1, r - 1)) % mod

        ones, ret, mod = 0, 0, 10 ** 9 + 7
        for b in s:
            n -= 1
            if b == '0':
                continue
            for x in good:
                left = x - ones
                if 0 <= left <= n:
                    ret = (ret + ncr(n, left)) % mod
            ones += 1
        return ret
