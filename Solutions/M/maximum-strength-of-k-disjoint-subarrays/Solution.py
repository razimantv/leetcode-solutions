# https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        # dp(i, j, inc) = max total from [i:] by taking j subarrays
        #                 if [i] is forced to be included or not
        n = len(nums)
        force, noforce = [-10 ** 15] * (k + 1), [-10 ** 15] * (k + 1)
        noforce[0] = 0
        for i in range(n - 1, -1, -1):
            sgn = -1
            for j in range(k, 0, -1):
                sgn = -sgn
                force[j] = sgn * j * nums[i] + max(force[j], noforce[j-1])
                noforce[j] = max(force[j], noforce[j])
        return noforce[k]
