# Minimum sum of values by dividing array

[Problem link](https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n, m = len(nums), len(andValues)
        first0 = [n] * 17
        ranges = [[] for _ in range(n)]

        for i in range(n-1, -1, -1):
            for b in range(17):
                if nums[i] & (1 << b) == 0:
                    first0[b] = i
            firsts = sorted(first0) + [n]

            for j, x in enumerate(andValues):
                mask = (1 << 17) - 1
                good = -1
                for p in firsts:
                    if p == n or (mask := mask & nums[p]) < x:
                        ranges[i]. append([] if good == -1 else [good, p])
                        break
                    if mask == x:
                        good = p

        base = 1
        while base < n:
            base <<= 1
        seg = [math. inf] * (2 * base + 1)
        seg[base + n] = 0

        def query(node, l, r, L, R):
            if l == L and r == R:
                return seg[node]
            M = (L + R) // 2
            if r <= M:
                return query(node*2, l, r, L, M)
            elif l > M:
                return query(node*2+1, l, r, M+1, R)
            else:
                return min(query(node*2, l, M, L, M), query(node*2+1, M+1, r, M+1, R))

        for j in range(m-1, -1, -1):
            for i in range(n):
                seg[base + i] = nums[i] + seg[base + i + 1]
            seg[base + n] = math. inf
            for i in range(base - 1, 0, -1):
                seg[i] = min(seg[2*i], seg[2*i+1])
            for i in range(n):
                if not ranges[i][j]:
                    seg[base + i] = math. inf
                else:
                    l, r = ranges[i][j]
                    seg[base+i] = query(1, l, r-1, 0, base-1)

        return seg[base] if seg[base] != math.inf else -1
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with bit value](/Collections/array-scanning.md#location-of-previous-element-with-bit-value)
* [Segment tree](/Collections/segment-tree.md#segment-tree)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
