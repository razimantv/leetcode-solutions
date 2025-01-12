# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n, psum = len(nums), [0] + list(accumulate(nums))
        next, mono = [n] * (n + 1), []
        for i in range(n - 1, -1, -1):
            while mono and nums[i] >= nums[mono[-1]]:
                mono.pop()
            if mono:
                next[i] = mono[-1]
            mono.append(i)

        lift = [[
            (j, (j - i) * x + psum[i] - psum[j])
            for i, (x, j) in enumerate(zip(nums, next))
        ] + [(n, 0)]]
        while min(prev := lift[-1])[0] < n:
            lift.append([
                (prev[j][0], x + prev[j][1]) for i, (j, x) in enumerate(prev)
            ])

        ret = 0
        for i in range(n):
            j, left = i, k
            for row in lift[::-1]:
                if row[j][1] <= left:
                    j, left = row[j][0], left - row[j][1]
            start, end = j, next[j]
            while end - start > 1:
                mid = (end + start) // 2
                if (mid + 1 - j) * nums[j] + psum[j] - psum[mid + 1] <= left:
                    start = mid
                else:
                    end = mid
            ret += min(start + 1, n) - i

        return ret
