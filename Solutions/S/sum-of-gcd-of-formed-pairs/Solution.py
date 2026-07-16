# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx, pref = 0, []
        for x in nums:
            mx = max(mx, x)
            pref.append(gcd(x,  mx))
        pref.sort()

        i, j, ret = 0, len(pref) - 1, 0
        while i < j:
            ret += gcd(pref[i], pref[j])
            i, j = i + 1, j - 1
        return ret
