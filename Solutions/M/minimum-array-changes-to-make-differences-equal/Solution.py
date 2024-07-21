# https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        pref = [0] * (k + 2)
        n = len(nums) // 2
        for i in range(n):
            x, y = nums[i], nums[-1-i]
            if x > y:
                x, y = y, x
            z = y - x
            pref[0] += 1
            pref[z] -= 1
            pref[z + 1] += 1
            pref[max(y, k - x) + 1] += 1
        return min(accumulate(pref))
