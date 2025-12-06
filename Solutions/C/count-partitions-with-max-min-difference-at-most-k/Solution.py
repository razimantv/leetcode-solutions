# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        asc, dsc, psum, mod = [], [], [0], 10 ** 9 + 7
        for i, x in enumerate(nums):
            while asc and nums[asc[-1]] <= x:
                asc.pop()
            asc.append(i)
            while dsc and nums[dsc[-1]] >= x:
                dsc.pop()
            dsc.append(i)

            if i == 0:
                cur = 1
            elif nums[asc[0]] - nums[dsc[0]] <= k:
                cur = 2 * (psum[-1] + mod - psum[-2]) % mod
            else:
                start, end, cur = 0, i, (psum[-1] + mod - psum[-2]) % mod
                while end - start > 1:
                    mid = (start + end) // 2
                    if (
                        nums[asc[bisect_left(asc, mid)]] -
                        nums[dsc[bisect_left(dsc, mid)]]
                    ) <= k:
                        end = mid
                    else:
                        start = mid

                if end < i:
                    cur = (cur + psum[-2] + mod - psum[end - 1]) % mod

            psum.append((psum[-1] + cur) % mod)

        return (psum[-1] + mod - psum[-2]) % mod
