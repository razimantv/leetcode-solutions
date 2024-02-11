# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        conv = [2 if x < y else 1 if x == y else 0 for x, y in pairwise(nums)]
        m = len(pattern)

        p1, p2, mod1, mod2 = 3, 5, 104983261, 216493713
        phash1, phash2 = 0, 0
        for x in pattern:
            phash1 = (phash1 * p1 + x + 1) % mod1
            phash2 = (phash2 * p2 + x + 1) % mod2

        cur1, sub1, cur2, sub2, ret = 0, 1, 0, 1, 0
        for i, x in enumerate(conv):
            cur1 = (cur1 * p1 + x) % mod1
            cur2 = (cur2 * p2 + x) % mod2
            if i >= m:
                cur1 = (cur1 + mod1 - (sub1 * conv[i - m]) % mod1) % mod1
                cur2 = (cur2 + mod2 - (sub2 * conv[i - m]) % mod2) % mod2
            else:
                sub1 = (sub1 * p1) % mod1
                sub2 = (sub2 * p2) % mod2

            if i >= m - 1 and cur1 == phash1 and cur2 == phash2:
                ret += 1

        return ret
