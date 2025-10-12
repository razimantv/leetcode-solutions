# https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences


MOD = 10 ** 9 + 7


@cache
def factorial(n):
    if n < 2:
        return 1
    return (n * factorial(n - 1)) % MOD


class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        n = len(nums)

        @cache
        def dp(i, m, k, mask):
            if i == n:
                return m == 0 and mask.bit_count() == k

            curpow, ret = 1, 0
            for j in range(m + 1):
                ret = (
                    ret +
                    dp(i + 1, m - j, k - ((mask + j) & 1), (mask + j) >> 1) *
                    curpow * pow(factorial(j), -1, MOD)
                ) % MOD
                curpow = (curpow * nums[i]) % MOD
            return ret

        return (dp(0, m, k, 0) * factorial(m)) % MOD
