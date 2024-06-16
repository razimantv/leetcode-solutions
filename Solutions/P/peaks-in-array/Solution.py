# https://leetcode.com/problems/peaks-in-array/

class Solution:
    def countOfPeaks(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(nums)
        nums.append(1 << 20)
        base = 1
        while base < n:
            base <<= 1
        seg = [0] * (base << 1)

        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                seg[base + i] = 1
        for i in range(base - 1, 0, -1):
            seg[i] = seg[2 * i] + seg[2 * i + 1]

        def update(i):
            newval = 1 if (
                nums[i] > nums[i - 1] and nums[i] > nums[i + 1]
            ) else 0
            i += base
            if seg[i] != newval:
                seg[i] = newval
                while i > 1:
                    i >>= 1
                    seg[i] = seg[2 * i] + seg[2 * i + 1]

        ret = []
        for q, a, b in queries:
            if q == 1:
                ret.append(0)
                if b - a < 2:
                    continue
                a, b = a + base, b + base - 1
                ret[-1] = seg[b] - seg[a]
                while a > 1:
                    if b & 1:
                        ret[-1] += seg[b ^ 1]
                    if a & 1:
                        ret[-1] -= seg[a ^ 1]
                    a, b = a >> 1, b >> 1
            else:
                nums[a] = b
                update(a)
                if a:
                    update(a - 1)
                if a < n - 1:
                    update(a + 1)

        return ret
