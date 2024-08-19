# https://leetcode.com/problems/2-keys-keyboard/

class Solution:
    @cache
    def f(self, n):
        if n == 1:
            return 0
        ret = n
        i = 2
        while i * i <= n:
            if n % i == 0:
                ret = min(ret, self.f(n // i) + i, self.f(i) + n // i)
            i += 1
        return ret

    def minSteps(self, n: int) -> int:
        return self.f(n)
