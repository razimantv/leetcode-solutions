# Minimum number of valid strings to form target ii

[Problem link](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        hbase, hmod = 43, 1027439813

        lmax = max(len(word) for word in words)
        hashes = [set() for _ in range(lmax)]
        hpow = [1]
        for i in range(lmax):
            hpow.append((hpow[-1] * hbase) % hmod)

        for word in words:
            h = 0
            for i, c in enumerate(word):
                h = (h + (ord(c) - ord('a')) * hpow[i]) % hmod
                hashes[i].add(h)

        base, n = 1, len(target)
        while base <= n:
            base <<= 1

        seg = [n + 1] * 2 * base

        def query(node, l, r, L, R):
            if l == L and r == R:
                return seg[node]
            M = (L + R) >> 1
            if r <= M:
                return query(node << 1, l, r, L, M)
            elif l > M:
                return query((node << 1) | 1, l, r, M + 1, R)
            else:
                return min(
                    query(node << 1, l, M, L, M),
                    query((node << 1) | 1, M + 1, r, M + 1, R)
                )

        def insert(node, x):
            seg[node] = x
            while node > 1:
                seg[node >> 1] = min(seg[node], seg[node ^ 1])
                node >>= 1

        insert(base + n, 0)
        hash = [0]
        for i in range(n - 1, -1, -1):
            hash.append((hash[-1] * hbase + ord(target[i]) - ord('a')) % hmod)
            start, end = 0, min(lmax, n - i) + 1
            while end - start > 1:
                mid = (start + end) >> 1
                if (
                    hash[-1] + hmod - (hash[-mid - 1] * hpow[mid]) % hmod
                ) % hmod in hashes[mid - 1]:
                    start = mid
                else:
                    end = mid

            if start:
                best = query(1, i + 1, i + start, 0, base - 1)
                insert(base + i, best + 1)

        return seg[base] if seg[base] <= n else -1
```
## Tags

* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Hashing](/Collections/string.md#hashing)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Segment tree](/Collections/dynamic-programming.md#segment-tree)
* [Segment tree](/Collections/segment-tree.md#segment-tree)
* [Binary search](/Collections/binary-search.md#binary-search)
