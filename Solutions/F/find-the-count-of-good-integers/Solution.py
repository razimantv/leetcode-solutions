# https://leetcode.com/problems/find-the-count-of-good-integers/

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        m = (n + 1) // 2
        seen = set()
        for left in range(10 ** (m - 1), 10 ** m):
            sl = str(left)
            sr = sl[-1-(n & 1)::-1]
            s = sl + sr
            if int(s) % k == 0:
                seen.add(tuple(sorted(list(Counter(s).items()))))

        fact = [1]
        for i in range(1, n + 1):
            fact.append(fact[-1] * i)

        ret = 0
        for ctr in seen:
            cur = fact[n]
            for k, v in ctr:
                cur //= fact[v]
            ret += cur

            if ctr[0][0] == '0':
                cur = fact[n - 1] // fact[ctr[0][1] - 1]
                for k, v in ctr[1:]:
                    cur //= fact[v]
                ret -= cur

        return ret
