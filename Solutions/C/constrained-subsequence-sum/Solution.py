# https://leetcode.com/problems/constrained-subsequence-sum/

from sortedcontainers import SortedDict


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        s = SortedDict([(0, 1)])
        ret = nums[0]
        pref = []
        for i, x in enumerate(nums):
            cur = x - s. keys()[0]
            ret = max(ret, cur)
            pref. append(-cur)
            s[-cur] = s.get(-cur, 0) + 1
            if i >= k:
                s[pref[i-k]] -= 1
                if not s[pref[i-k]]:
                    del s[pref[i-k]]
        return ret
