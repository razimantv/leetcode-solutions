# https://leetcode.com/problems/count-the-number-of-good-partitions/

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        lim = {}
        for i, x in enumerate(nums):
            if x not in lim:
                lim[x] = [i, i]
            else:
                lim[x][1] = i

        pref = [0] * n
        for x, (s, e) in lim.items():
            pref[s] += 1
            pref[e] -= 1

        ret, psum, MOD = 1, 0, 10 ** 9 + 7
        for x in pref[:-1]:
            psum += x
            if not psum:
                ret = (ret * 2) % MOD
        return ret
