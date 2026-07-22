# https://leetcode.com/problems/maximize-active-section-with-trade-ii/

class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: list[list[int]]
    ) -> list[int]:
        zeros, starts = [], []
        cur = -1
        for i, c in enumerate(s):
            if c == '1':
                cur = -1
            else: 
                if cur == -1:
                    cur = i
                    starts.append(cur)
                    zeros.append(1)
                else:
                    zeros[-1] = i - cur + 1

        zp = [x + y for x, y in pairwise(zeros)]
        m, base = len(zp), 1
        while base < m:
            base <<= 1
        seg = [0] * (base << 1)
        seg[base:base + m] = zp
        for i in range(base - 1, 0, -1):
            seg[i] = max(seg[i << 1], seg[(i << 1) | 1])

        def query(node, l, r, L, R):
            if l == L and r == R:
                return seg[node]
            M, lc, rc = (L + R) >> 1, node << 1, (node << 1) | 1
            if r <= M:
                return query(lc, l, r, L, M)
            elif l > M:
                return query(rc, l, r, M + 1, R)
            else: 
                return max(query(lc, l, M, L, M), query(rc, M + 1, r, M + 1, R))
 
        def work(l, r):
            if not starts:
                return 0
                
            p1, p2 = bisect_right(starts, l), bisect_right(starts, r) - 1
            if p1 > 0 and starts[p1 - 1] + zeros[p1 - 1] - 1 >= l:
                p1 -= 1
            if p2 <= p1:
                return 0
                
            len1 = min(r, starts[p1] + zeros[p1] - 1) - max(l, starts[p1]) + 1
            len2 = min(r, starts[p2] + zeros[p2] - 1) - max(l, starts[p2]) + 1
            if p2 == p1 + 1:
                return len1 + len2
                
            ret = max(len1 + zeros[p1 + 1], zeros[p2 - 1] + len2)
            if p2 - 1 > p1 + 1:
                ret = max(ret, query(1, p1 + 1, p2 - 2, 0, base - 1))
            return ret

        base_ones = s.count('1')
        return [base_ones + work(l, r) for l, r in queries]
