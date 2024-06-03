# https://leetcode.com/problems/count-good-triplets-in-an-array


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        inv1 = [0] * n
        for i, x in enumerate(nums1):
            inv1[x] = i

        base = 1
        while base < n:
            base *= 2

        seg = [[0, 0] for _ in range(2 * base)]
        ret = 0
        for x in nums2:
            node, c0, c1 = inv1[x] + base, 0, 0
            while node > 1:
                if node & 1:
                    c0 += seg[node ^ 1][0]
                    c1 += seg[node ^ 1][1]
                node //= 2
            ret += c1
            node = inv1[x] + base
            while node:
                seg[node][0] += 1
                seg[node][1] += c0
                node //= 2

        return ret
