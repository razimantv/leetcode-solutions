# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/
from sortedcontainers import SortedList


class Solution:
    def getFinalState(
        self, nums: List[int], k: int, multiplier: int
    ) -> List[int]:
        if multiplier == 1:
            return nums

        sl = SortedList([(x, i) for i, x in enumerate(nums)])
        mx = sl[-1][0]
        while k and sl[0][0] * multiplier <= mx:
            k -= 1
            x, i = sl.pop(0)
            sl.add((x * multiplier, i))

        def modpow(a, n, mod):
            ret = 1
            while n:
                if n & 1:
                    ret = (ret * a) % mod
                a = (a * a) % mod
                n >>= 1
            return ret

        n, mod = len(nums), 10 ** 9 + 7
        pow = k // n
        mxmult = modpow(multiplier, pow, mod)
        for x, i in sl:
            cur = k // n + (k % n > 0)
            if cur == pow:
                nums[i] = (x * mxmult) % mod
            else:
                nums[i] = (x * mxmult * multiplier) % mod
            k, n = k - cur, n - 1
        return nums
