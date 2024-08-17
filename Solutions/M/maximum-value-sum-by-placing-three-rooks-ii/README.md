# Maximum value sum by placing three rooks ii

[Problem link](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        n, inf, best = len(board[0]), -10 ** 11, []

        base = 1
        while base < n:
            base <<= 1
        seg = [inf] * (2 * base)

        def update(node, L, R, l, r, cur):
            if L == l and R == r:
                seg[node] = max(seg[node], cur)
                return
            lc, rc, M = 2 * node, 2 * node + 1, (L + R) >> 1
            if M >= r:
                update(lc, L, M, l, r, cur)
            elif M < l:
                update(rc, M + 1, R, l, r, cur)
            else:
                update(lc, L, M, l, M, cur)
                update(rc, M + 1, R, M + 1, r, cur)

        def bestwithout(i):
            node = i + base
            ret = seg[node]
            while node > 1:
                node >>= 1
                ret = max(ret, seg[node])
            return ret

        def get3(ar):
            ret = sorted([(x, i) for i, x in enumerate(ar[:3])])
            for i in range(3, n):
                cur = (ar[i], i)
                if cur > ret[2]:
                    ret = [ret[1], ret[2], cur]
                elif cur > ret[1]:
                    ret = [ret[1], cur, ret[2]]
                elif cur > ret[0]:
                    ret = [cur, ret[1], ret[2]]
            return ret

        ret = inf
        for row in board:
            best3 = get3(row)
            for x, i in best3:
                ret = max(ret, bestwithout(i) + x)

            for x, i in best3:
                for y, j in best:
                    if i == j:
                        continue
                    l, r = (i, j) if i < j else (j, i)
                    cur = x + y
                    if l:
                        update(1, 0, base - 1, 0, l - 1, cur)
                    if r > l + 1:
                        update(1, 0, base - 1, l + 1, r - 1, cur)
                    if r < n - 1:
                        update(1, 0, base - 1, r + 1, n - 1, cur)

            for x, i in best3:
                for c, (y, j) in enumerate(best):
                    if i == j:
                        best[c] = (max(x, y), i)
                        break
                else:
                    best.append((x, i))
            best = sorted(best)[-3:]

        return ret
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree)
* [Greedy](/Collections/greedy.md#greedy)
