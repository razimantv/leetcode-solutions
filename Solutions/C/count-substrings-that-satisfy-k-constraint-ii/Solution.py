# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n, base = len(s), 1
        while base < n:
            base <<= 1
        seg, lazy = [0] * (2 * base), [0] * (2 * base)

        def merge(node, n):
            if lazy[node]:
                seg[node] += lazy[node] * n
                if node < base:
                    lazy[node * 2] += lazy[node]
                    lazy[node * 2 + 1] += lazy[node]
                lazy[node] = 0

        def update(node, L, R, l, r):
            merge(node, R - L + 1)
            if L == l and R == r:
                lazy[node] -= 1
                return
            M, lc, rc = (L + R) // 2, 2 * node, 2 * node + 1
            seg[node] -= (r - l + 1)
            if M >= r:
                update(lc, L, M, l, r)
            elif M < l:
                update(rc, M + 1, R, l, r)
            else:
                update(lc, L, M, l, M)
                update(rc, M + 1, R, M + 1, r)

        def query(node, L, R, l, r):
            merge(node, R - L + 1)
            if L == l and R == r:
                return seg[node]
            M, lc, rc = (L + R) // 2, 2 * node, 2 * node + 1
            if M >= r:
                return query(lc, L, M, l, r)
            elif M < l:
                return query(rc, M + 1, R, l, r)
            else:
                return query(lc, L, M, l, M) + query(rc, M + 1, R, M + 1, r)

        def countlongest(s):
            last0, last1 = defaultdict(lambda: -2), defaultdict(lambda: -2)
            last0[0] = last1[0] = -1
            cnt0, cnt1 = 0, 0
            ret = [0] * n

            for i, c in enumerate(s):
                if c == '0':
                    cnt0 += 1
                else:
                    cnt1 += 1
                last0[cnt0], last1[cnt1] = i, i
                ret[i] = i - min(last0[cnt0 - k - 1], last1[cnt1 - k - 1]) - 1

            return ret

        seg[base:base+n] = countlongest(s)
        for i in range(base - 1, 0, -1):
            seg[i] = seg[2 * i] + seg[2 * i + 1]
        rev = countlongest(s[::-1])[::-1]

        queries = sorted([[q, i] for i, q in enumerate(queries)])
        ret, last = [0] * len(queries), 0
        for (l, r), q in queries:
            while last < l:
                update(1, 0, base - 1, last, last + rev[last] - 1)
                last += 1
            ret[q] = query(1, 0, base - 1, l, r)

        return ret
