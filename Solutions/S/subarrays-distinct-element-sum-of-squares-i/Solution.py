# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        base = 1
        while base < n:
            base <<= 1

        seg = [[0, 0, 0] for _ in range(base << 1)]

        def lazyfix(node, L, R):
            totsq, tot, lazy = seg[node]
            cnt = R - L + 1
            if lazy:
                if node < base:
                    seg[node << 1][2] += lazy
                    seg[(node << 1) | 1][2] += lazy
                while lazy:
                    totsq += 2 * tot + cnt
                    tot += cnt
                    lazy -= 1
            seg[node] = [totsq, tot, lazy]

        def update(node, L, R, l, r):
            # lazy: processing has not been done for this node

            if l == L and r == R:
                seg[node][2] += 1

            if seg[node][2]:
                lazyfix(node, L, R)

            if l == L and r == R:
                return

            M = (L + R) >> 1
            lc = node << 1
            rc = lc | 1

            if seg[lc][2]:
                lazyfix(lc, L, M)
            if seg[rc][2]:
                lazyfix(rc, M+1, R)

            if r <= M:
                update(lc, L, M, l, r)
            elif l > M:
                update(rc, M+1, R, l, r)
            else:
                update(lc, L, M, l, M)
                update(rc, M+1, R, M+1, r)

            seg[node] = [seg[lc][0] + seg[rc][0], seg[lc][1] + seg[rc][1], 0]

        last = {}
        ret = 0
        for i, x in enumerate(nums):
            start = last[x] + 1 if x in last else 0
            update(1, 0, base-1, start, i)
            ret += seg[1][0]
            last[x] = i

        return ret % 1000000007
