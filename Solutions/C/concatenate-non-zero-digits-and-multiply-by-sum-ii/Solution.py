# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        digcnt, digsum, dignum = [[0] for _ in range(3)]
        mod = 10 ** 9 + 7
        for c in s:
            if c == '0':
                for ar in [digcnt, digsum, dignum]:
                    ar.append(ar[-1])
            else:
                d = int(c)
                digcnt.append(digcnt[-1] + 1)
                digsum.append(digsum[-1] + d)
                dignum.append((dignum[-1] * 10 + d) % mod)
        
        return [
            (
                (
                    dignum[r + 1] + mod -
                    dignum[l] * pow(10, digcnt[r + 1] - digcnt[l], mod)
                ) * (digsum[r + 1] - digsum[l])
            ) % mod for l, r in queries
        ]
