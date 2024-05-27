# https://leetcode.com/problems/block-placement-queries/

from sortedcontainers import SortedList


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        n = max(query[1] for query in queries) + 3
        base = 1
        while n > base:
            base <<= 1

        seg = [0] * (base << 1)
        lazy = [0] * (base << 1)
        for i in range(n):
            seg[base + i] = i + 1
        for i in range(base - 1, 0, -1):
            seg[i] = max(seg[2 * i:2 * i + 2])

        def update(node, l, r, L, R, val):
            if (l, r) == (L, R):
                lazy[node] += val
                return

            lc, rc, M = 2 * node, 2 * node + 1, (L + R) // 2
            if lazy[node]:
                seg[node] += lazy[node]
                lazy[lc] += lazy[node]
                lazy[rc] += lazy[node]
                lazy[node] = 0

            if r <= M:
                update(lc, l, r, L, M, val)
            elif l > M:
                update(rc, l, r, M + 1, R, val)
            else:
                update(lc, l, M, L, M, val)
                update(rc, M + 1, r, M + 1, R, val)
            seg[node] = max(seg[lc] + lazy[lc], seg[rc] + lazy[rc])

        def query(node, l, r, L, R):
            if (l, r) == (L, R):
                return seg[node] + lazy[node]
            lc, rc, M = 2 * node, 2 * node + 1, (L + R) // 2
            if lazy[node]:
                seg[node] += lazy[node]
                lazy[lc] += lazy[node]
                lazy[rc] += lazy[node]
                lazy[node] = 0

            if r <= M:
                return query(lc, l, r, L, M)
            elif l > M:
                return query(rc, l, r, M + 1, R)
            else:
                return max(
                    query(lc, l, M, L, M),
                    query(rc, M + 1, r, M + 1, R)
                )

        ret = []
        used = SortedList([n - 2])
        for q in queries:
            x = q[1]
            if q[0] == 1:
                cur = query(1, x, x, 0, base - 1)
                next = used[used. bisect_right(x)]
                used. add(x)
                update(1, x, next - 1, 0, base - 1, 1 - cur)
            else:
                cur = query(1, 0, x - 1, 0, base - 1)
                ret. append(cur >= q[2])
        return ret
