# https://leetcode.com/problems/sorted-gcd-pair-queries/

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        nmax = max(nums)
        gcnt, ctr = [0] * (nmax + 1), [0] * (nmax + 1)
        for x in nums:
            ctr[x] += 1

        for i in range(nmax, 0, -1):
            j, cur = i, 0
            for j in range(i, nmax + 1, i):
                gcnt[i] -= gcnt[j]
                cur += ctr[j]
            gcnt[i] += cur * (cur - 1) // 2

        psum = list(accumulate(gcnt))
        return [bisect_right(psum, q) for q in queries]
