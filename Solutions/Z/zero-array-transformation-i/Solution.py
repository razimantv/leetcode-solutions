# https://leetcode.com/problems/zero-array-transformation-i/

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)

        def poss(k):
            pref = [0] * (n+1)
            for l, r in queries[:k]:
                delta = 1
                pref[l] += delta
                pref[r+1] -= delta
            cur = 0
            for x, y in zip(nums, pref):
                cur += y
                if x > cur:
                    return False
            return True

        return poss(q)
