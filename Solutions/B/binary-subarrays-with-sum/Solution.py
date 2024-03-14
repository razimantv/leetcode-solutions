# https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref, cnt, ret = 1, defaultdict(int), 0
        for x in nums:
            cnt[pref] += 1
            pref += x
            ret += cnt[pref - goal]
        return ret
