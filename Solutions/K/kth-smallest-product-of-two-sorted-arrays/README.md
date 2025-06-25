# Kth smallest product of two sorted arrays

[Problem link](https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

class Solution:
    def kthSmallestProduct(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> int:
        def signs(ar):
            N, P = [[x * s for x in ar if x * s > 0] for s in (-1, 1)]
            m, n, p = len(ar), len(N), len(P)
            return [m, n, m - n - p, p, N[::-1], P]

        def count(ar1, ar2, limit):
            j, ret = len(ar2) - 1, 0
            for i, x in enumerate(ar1):
                while j >= 0 and x * ar2[j] > limit:
                    j -= 1
                ret += j + 1
            return ret

        def work(a1, b1, a2, b2, k):
            # Find the kth smallest product among a1 * a2, b1 * b2
            # invariant: count(start) < k, count(end) >= k
            start, end = 0, 10 ** 10
            while end - start > 1:
                mid = (end + start) >> 1
                if count(a1, a2, mid) + count(b1, b2, mid) < k:
                    start = mid
                else:
                    end = mid
            return end

        m1, n1, z1, p1, N1, P1 = signs(nums1)
        m2, n2, z2, p2, N2, P2 = signs(nums2)

        negs = n1 * p2 + p1 * n2
        zeros = z1 * m2 + z2 * m1 - z1 * z2
        if negs >= k:
            return -work(N1, P1, P2, N2, negs - k + 1)

        k -= negs
        if zeros >= k:
            return 0

        k -= zeros
        return work(N1, P1, N2, P2, k)
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
* [Binary search](/Collections/binary-search.md#binary-search)
