# https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count(n):
            s = '0' + "{0:b}".format(n)
            l = len(s)
            ret = 0
            for i in range(x-1, l-1, x):
                j = l - 1 - i
                pref = int(s[:j], 2)
                suf = int(s[j+1:], 2) if j < l-1 else 0
                allsuf = 1 << (l - 1 - j)
                ret += pref * allsuf
                if s[j] == '1':
                    ret += suf + 1
            return ret

        start, end = 1, 1
        while count(end) <= k:
            end <<= 1
        while (end - start) > 1:
            mid = (end + start) >> 1
            if count(mid) <= k:
                start = mid
            else:
                end = mid
        return start
