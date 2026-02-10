# Longest balanced subarray ii

[Problem link](https://leetcode.com/problems/longest-balanced-subarray-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/longest-balanced-subarray-ii/

class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n, last, base = len(nums), {}, 1
        while base < n:
            base <<= 1
        smin, smax, lazy = [[0] * (base << 1) for _ in (0, 1, 2)]

        def split(node):
            if not lazy[node]:
                return
            for ar in [smin, smax, lazy]:
                for dc in (0, 1):
                    ar[(node << 1) | dc] += lazy[node]
            lazy[node] = 0

        def update(node, l, r, L, R, delta):
            if (l, r) == (L, R):
                for ar in [smin, smax, lazy]:
                    ar[node] += delta
                return

            split(node)
            M, lc, rc = (L + R) >> 1, (node << 1), (node << 1) | 1
            if l <= M:
                update(lc, l, min(r, M), L, M, delta)
            if r > M:
                update(rc, max(l, M + 1), r, M + 1, R, delta)
            smin[node] = min(smin[lc], smin[rc])
            smax[node] = max(smax[lc], smax[rc])

        def query(node, L, R, i):
            while node < base:
                split(node)
                node <<= 1
                M = (L + R) >> 1
                if i > M:
                    node |= 1
                    L = M + 1
                else:
                    R = M
            return smin[node]

        def bs(node, val):
            while node < base:
                split(node)
                node <<= 1
                if not (smin[node] <= val <= smax[node]):
                    node |= 1

            return node - base

        ret = 0
        for i, x in enumerate(nums):
            delta = 1 if x & 1 else -1
            if x in last:
                update(1, last[x], base - 1, 0, base - 1, -delta)
            last[x] = i
            update(1, i, base - 1, 0, base - 1, delta)
            psum = query(1, 0, base - 1, i)
            if not psum:
                ret = i + 1
            else:
                ret = max(ret, i - bs(1, psum))
        return ret
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree) > [Lazy propagation](/Collections/segment-tree.md#lazy-propagation)
* [Segment tree](/Collections/segment-tree.md#segment-tree) > [Binary search](/Collections/segment-tree.md#binary-search)
* [Binary search](/Collections/binary-search.md#binary-search) > [Segment tree](/Collections/binary-search.md#segment-tree)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with same value](/Collections/array-scanning.md#location-of-previous-element-with-same-value)
