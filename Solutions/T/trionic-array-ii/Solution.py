# https://leetcode.com/problems/trionic-array-ii

class Solution:
    def maxSumTrionic(self, nums: list[int]) -> int:
        n, (start, end) = len(nums), [[[-1] * 3 for _ in nums] for se in 'se']
        for i, (x, y) in enumerate(pairwise(nums)):
            if y > x:
                start[i + 1][0] = start[i][0] if start[i][0] != -1 else i
                start[i + 1][2] = max(start[i][1:])
                end[i + 1][0] = i
                end[i + 1][2] = max(end[i][1:])
            elif y < x:
                start[i + 1][1] = max(start[i][:2])
                end[i + 1][1] = max(end[i][:2])

        base = 1
        while base <= n:
            base <<= 1
        seg = [0] * (base << 1)
        seg[base + 1: base + n + 1] = list(accumulate(nums))

        for i in range(base - 1, 0, -1):
            seg[i] = min(seg[i << 1], seg[(i << 1) | 1])

        def query(node, l, r, L, R):
            if l == L and r == R:
                return seg[node]
            M = (L + R) >> 1
            if l > M:
                return query((node << 1) | 1, l, r, M + 1, R)
            elif r <= M:
                return query(node << 1, l, r, L, M)
            else:
                return min(
                    query(node << 1, l, M, L, M),
                    query((node << 1) | 1, M + 1, r, M + 1, R)
                )

        ret = -inf
        for i in range(n):
            if start[i][2] == -1:
                continue
            l, r = start[i][2], end[i][2]
            ret = max(ret, seg[base + i + 1] - query(1, l, r, 0, base - 1))
        return ret
