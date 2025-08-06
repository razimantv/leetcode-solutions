# https://leetcode.com/problems/fruits-into-baskets-iii/

class Solution:
    def numOfUnplacedFruits(
        self, fruits: list[int], baskets: list[int]
    ) -> int:
        n, base, ret = len(baskets), 1, 0
        while base < n:
            base <<= 1

        seg = [0] * (base << 1)
        seg[base:base + n] = baskets
        for i in range(base - 1, 0, -1):
            seg[i] = max(seg[i << 1], seg[(i << 1) | 1])

        for x in fruits:
            if seg[1] < x:
                ret += 1
                continue
            node = 1
            while node < base:
                lc = node << 1
                node = lc if seg[lc] >= x else (lc | 1)
            seg[node] = 0
            while node > 1:
                seg[node >> 1] = max(seg[node], seg[node ^ 1])
                node >>= 1

        return ret
