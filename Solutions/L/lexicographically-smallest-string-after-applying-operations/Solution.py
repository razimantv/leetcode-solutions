# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        s = [int(c) for c in s]
        n, s, ret = len(s), s + s, s
        for i in range(0, n, gcd(n, b)):
            t = s[i:i + n]
            add = t[1] % gcd(10, a) + 10 - t[1]
            for j in range(1, n, 2):
                t[j] = (t[j] + add) % 10
            if b & 1:
                add = t[0] % gcd(10, a) + 10 - t[0]
                for j in range(0, n, 2):
                    t[j] = (t[j] + add) % 10
            ret = min(ret, t)
        return ''.join([str(x) for x in ret])
