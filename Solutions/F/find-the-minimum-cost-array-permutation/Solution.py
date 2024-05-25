# https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [[-1] * n for _ in range(1 << n)]

        def work(i, j, mask):
            if dp[mask][j] != -1:
                return dp[mask][j]
            elif i == n - 1:
                return (abs(j - nums[0]), -1)
            ret = (math.inf, -1)
            for k in range(n):
                if mask & (1 << k):
                    continue
                val, next = work(i + 1, k, mask ^ (1 << k))
                val += abs(j - nums[k])
                if val < ret[0]:
                    ret = (val, k)
            dp[mask][j] = ret
            return ret

        work(0, 0, 1)
        ret, mask = [0], 1
        for i in range(1, n):
            next = dp[mask][ret[-1]][1]
            ret.append(next)
            mask |= (1 << next)
        return ret
