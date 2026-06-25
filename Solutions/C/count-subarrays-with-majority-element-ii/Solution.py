# https://leetcode.com/problems/count-subarrays-with-majority-element-ii

class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        psum = [0] + list(accumulate((1 if x == target else -1 for x in nums)))
        l, r = min(psum), max(psum)
        n, base, ret = r - l + 1, 1, 0
        while base < n:
            base <<= 1
        seg = [0] * (base << 1)

        for x in psum:
            node = base + x - l
            while node > 1:
                seg[node] += 1
                if node & 1:
                    ret += seg[node ^ 1]
                node >>= 1
        return ret
