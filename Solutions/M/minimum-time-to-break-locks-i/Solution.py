# https://leetcode.com/problems/minimum-time-to-break-locks-i

class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        n = len(strength)

        def work(ar):
            t, X = 0, 1
            for x in ar:
                t += (x + X - 1) // X
                X += K
            return t

        return min(work(perm) for perm in permutations(strength))
