# https://leetcode.com/problems/find-products-of-elements-of-big-array/

class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        def cntsum(n):
            cnt, tot = 0, 0
            bit, p = 1, 0
            while bit < n:
                bit, p = bit << 1, p + 1

            while p >= 0:
                if n & bit:
                    n ^= bit
                    cnt += bit * p // 2 + n + 1
                    tot += bit * p * (p - 1) // 4 + (n + 1) * p
                bit, p = bit >> 1, p - 1
            return cnt, tot

        def rangesum(n):
            start, end = 0, n
            while end - start > 1:
                mid = (start + end) >> 1
                if cntsum(mid)[0] >= n:
                    end = mid
                else:
                    start = mid

            cnt, tot = cntsum(end)
            bit, p = 1, 0
            while bit < end:
                bit, p = bit << 1, p + 1
            while cnt > n:
                if end & bit:
                    cnt -= 1
                    tot -= p
                bit, p = bit >> 1, p - 1
            return tot

        def modpow(a, b, mod):
            ret = 1
            while b:
                if b & 1:
                    ret = (ret * a) % mod
                a = (a * a) % mod
                b >>= 1
            return ret % mod

        for i, (l, r, mod) in enumerate(queries):
            queries[i] = modpow(2, rangesum(r + 1) - rangesum(l), mod)
        return queries
