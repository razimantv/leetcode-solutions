# https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        elif min(nums) >= 0:
            return sum(nums)

        n, base, pos = len(nums), 1, defaultdict(list)
        while base < n:
            base <<= 1
        seg = [[0] * 4 for _ in range(2 * base)]
        for i, x in enumerate(nums):
            seg[base + i] = [x] * 4
            if x < 0:
                pos[x].append(i)

        def merge(l, r):
            (ltot, lmax, ll, lr), (rtot, rmax, rl, rr) = l, r
            return [
                ltot + rtot, max(lmax, rmax, lr + rl),
                max(ll, ltot + rl), max(rr, rtot + lr)
            ]

        def query(node, l, r, L, R):
            if l == L and r == R:
                return seg[node]
            M, lc = (L + R) >> 1, node << 1
            if r <= M:
                return query(lc, l, r, L, M)
            elif l > M:
                return query(lc | 1, l, r, M + 1, R)
            else:
                return merge(
                    query(lc, l, M, L, M), query(lc | 1, M + 1, r, M + 1, R)
                )

        for node in range(base - 1, 0, -1):
            seg[node] = merge(seg[2 * node], seg[2 * node + 1])

        ret = 0
        for k, v in pos.items():
            cur = [0, 0, 0, 0]
            for i, j in pairwise(chain([-1], v, [n])):
                if j == i + 1:
                    continue
                cur = merge(cur, query(1, i + 1, j - 1, 0, base - 1))
            ret = max(ret, cur[1])
        return ret
