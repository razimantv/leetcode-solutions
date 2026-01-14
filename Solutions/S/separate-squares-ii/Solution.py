# https://leetcode.com/problems/separate-squares-ii

class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        events = sorted([
            (y + (1 - delta) // 2 * l, delta, x, x + l)
            for x, y, l in squares for delta in (1, -1)
        ])
        xs = list(sorted([x + l * d for x, y, l in squares for d in (0, 1)]))

        n, base = len(xs) - 1, 1
        while base < n:
            base <<= 1
        cover, length = [[0] * (base << 1) for _ in (0, 1)]
        xs += [xs[-1] + 1] * (base - n + 1)

        def update(node, l, r, x1, x2, delta):
            if xs[l] >= x2 or xs[r + 1] <= x1:
                return
            if xs[l] == x1 and xs[r + 1] == x2:
                cover[node] += delta
            else:
                m = (l + r) // 2
                update(node << 1, l, m, x1, min(x2, xs[m + 1]), delta)
                update(
                    (node << 1) | 1, m + 1, r, max(x1, xs[m + 1]), x2, delta
                )

            if cover[node]:
                length[node] = (xs[r + 1] - xs[l])
            elif l == r:
                length[node] = 0
            else:
                length[node] = length[node << 1] + length[(node << 1) | 1]

        yprev, psum = events[0][0], [0]
        for y, delta, x1, x2 in events:
            psum.append(psum[-1] + length[1] * (y - yprev))
            update(1, 0, base - 1, x1, x2, delta)
            yprev = y

        idx = bisect_left(psum, target := (psum[-1] / 2))
        x1, x2 = psum[idx - 1], psum[idx],
        y1, y2 = events[idx - 2][0], events[idx - 1][0]
        return y1 + (y2 - y1) * ((target - x1) / (x2 - x1))
