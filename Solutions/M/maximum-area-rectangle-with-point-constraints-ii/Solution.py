# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        compress = {x: i for i, x in enumerate(sorted(list(set(xCoord))))}
        n = len(compress)
        base = 1
        while base < n:
            base <<= 1
        seg = [-1] * (2 * base)

        rows = defaultdict(list)
        for x, y in zip(xCoord, yCoord):
            rows[y].append(x)

        def query(node, L, R, l, r):
            if l == L and r == R:
                return seg[node]
            lc, rc, M = node << 1, (node << 1) | 1, (L + R) >> 1
            if r <= M:
                return query(lc, L, M, l, r)
            elif l > M:
                return query(rc, M + 1, R, l, r)
            else:
                return max(
                    query(lc, L, M, l, M), query(rc, M + 1, R, M + 1, r)
                )

        ret = -1
        for y, xvec in sorted(rows.items()):
            for x1, x2 in pairwise(sorted(xvec)):
                c1, c2 = compress[x1], compress[x2]
                y1, y2 = seg[base + c1], seg[base + c2]
                if y1 == -1 or y1 != y2:
                    continue
                if c2 > c1 + 1 and query(1, 0, base - 1, c1 + 1, c2 - 1) >= y1:
                    continue
                ret = max(ret, (x2 - x1) * (y - y1))
            for x in xvec:
                c = base + compress[x]
                while c:
                    seg[c] = y
                    c >>= 1
        return ret
