# https://leetcode.com/problems/find-the-original-typed-string-ii/

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        groups = []
        cur, ret, mod = 1, 1, 10 ** 9 + 7
        for c, d in pairwise(word):
            if c == d:
                cur += 1
            else:
                groups.append(cur)
                ret = (ret * cur) % mod
                cur = 1
        groups.append(cur)
        ret = (ret * cur) % mod

        if len(groups) >= k:
            return ret

        dp = [1] + [0] * (k - 1)
        for x in groups:
            newdp = [0] * k
            psum = [0] + list(accumulate(dp))
            for i in range(k):
                newdp[i] = psum[i] % mod
                if i >= x:
                    newdp[i] = (newdp[i] + mod - psum[i - x]) % mod
            dp = newdp

        return (ret + mod - sum(dp) % mod) % mod
