# https://leetcode.com/problems/maximum-good-subarray-sum/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        best = {}
        pref, ret = 0, None
        for i, x in enumerate(nums):
            if x not in best or best[x] > pref:
                best[x] = pref
            pref += x
            for target in [x - k, x + k]:
                if target in best:
                    cur = pref - best[target]
                    if ret is None or ret < cur:
                        ret = cur
        return 0 if ret is None else ret
