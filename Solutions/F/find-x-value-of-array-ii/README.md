# Find x value of array ii

[Problem link](https://leetcode.com/problems/find-x-value-of-array-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-x-value-of-array-ii/


class Seg:
    def __init__(self, k):
        self.k = k
        self.all = 1
        self.first = [0] * k


def merge(s1, s2):
    k = s1.k
    ret = Seg(k)
    ret.all = (s1.all * s2.all) % k
    for i in range(k):
        ret.first[i] += s1.first[i]
        ij = (i * s1.all) % k
        ret.first[ij] += s2.first[i]
    return ret


class Solution:
    def resultArray(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[int]:
        n, base = len(nums), 1
        while base < n:
            base <<= 1
        seg = [Seg(k) for _ in range(base << 1)]

        for i, x in enumerate(nums):
            si, x = seg[base + i], x % k
            si.all = x
            si.first[x] = 1
        for i in range(base - 1, 0, -1):
            seg[i] = merge(seg[2 * i], seg[2 * i + 1])

        def query(node, L, R, l, r):
            if (L, R) == (l, r):
                return seg[node]
            M, lc, rc = (L + R) >> 1, node << 1, (node << 1) | 1
            if r <= M:
                return query(lc, L, M, l, r)
            elif l > M:
                return query(rc, M + 1, R, l, r)
            else:
                return merge(
                    query(lc, L, M, l, M), query(rc, M + 1, R, M + 1, r)
                )

        ret = []
        for i, v, s, x in queries:
            i, v = i + base, v % k
            si = seg[i] = Seg(k)
            si.all = v
            si.first[v] = 1
            while i > 1:
                i >>= 1
                seg[i] = merge(seg[2 * i], seg[2 * i + 1])
            ret.append(query(1, 0, base - 1, s, n - 1).first[x])
        return ret
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree)
