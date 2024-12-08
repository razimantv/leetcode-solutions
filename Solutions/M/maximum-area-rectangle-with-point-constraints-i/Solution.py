# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/

class QuadNode:
    def __init__(self):
        self.cnt = 0
        self.child = [[None, None], [None, None]]


class Solution:
    def maxRectangleArea(self, coord) -> int:
        xCoord = [xy[0] for xy in coord]
        yCoord = [xy[1] for xy in coord]
        quad = QuadNode()
        xmin, xmax = min(xCoord), max(xCoord)
        ymin, ymax = min(yCoord), max(yCoord)

        def insert(node, xl, xr, yl, yr, x, y):
            node.cnt += 1
            if xl == xr and yl == yr:
                return
            xm, ym = (xl + xr) // 2, (yl + yr) // 2
            if x <= xm:
                i = 0
                cxl, cxr = xl, xm
            else:
                i = 1
                cxl, cxr = xm + 1, xr
            if y <= ym:
                j = 0
                cyl, cyr = yl, ym
            else:
                j = 1
                cyl, cyr = ym + 1, yr

            if node.child[i][j] is None:
                node.child[i][j] = QuadNode()
            insert(node.child[i][j], cxl, cxr, cyl, cyr, x, y)

        def count(node, xl, xr, yl, yr, xL, xR, yL, yR, cur):
            if cur > 4:
                return 5
            if xL <= xl and xr <= xR and yL <= yl and yr <= yR:
                return cur + node.cnt
            xm, ym = (xl + xr) // 2, (yl + yr) // 2
            if xm >= xL and ym >= yL:
                i, j = 0, 0
                if node.child[i][j] is not None:
                    cur = count(
                        node.child[i][j], xl, xm, yl, ym,
                        xL, min(xm, xR), yL, min(ym, yR), cur
                    )
                    if cur > 4:
                        return 5
            if xm >= xL and ym < yR:
                i, j = 0, 1
                if node.child[i][j] is not None:
                    cur = count(
                        node.child[i][j], xl, xm, ym + 1, yr,
                        xL, min(xm, xR), max(ym + 1, yL), yR, cur
                    )
                    if cur > 4:
                        return 5
            if xm < xR and ym >= yL:
                i, j = 1, 0
                if node.child[i][j] is not None:
                    cur = count(
                        node.child[i][j], xm + 1, xr, yl, ym,
                        max(xm + 1, xL), xR, yL, min(ym, yR), cur
                    )
                    if cur > 4:
                        return 5
            if xm < xR and ym < yR:
                i, j = 1, 1
                if node.child[i][j] is not None:
                    cur = count(
                        node.child[i][j], xm + 1, xr, ym + 1, yr,
                        max(xm + 1, xL), xR, max(ym + 1, yL), yR, cur
                    )
                    if cur > 4:
                        return 5
            return cur

        rows, cols = defaultdict(list), defaultdict(list)
        seen = set()
        for x, y in zip(xCoord, yCoord):
            insert(quad, xmin, xmax, ymin, ymax, x, y)
            seen.add((x, y))
            rows[x].append(y)
            cols[y].append(x)

        rownext, colnext = {}, {}
        for x, row in rows.items():
            for y1, y2 in pairwise(sorted(row)):
                rownext[(x, y1)] = y2
        for y, col in cols.items():
            for x1, x2 in pairwise(sorted(col)):
                colnext[(x1, y)] = x2

        ret = -1
        for x, y in zip(xCoord, yCoord):
            if (x, y) not in rownext:
                continue
            else:
                y2 = rownext[(x, y)]
            if (x, y) not in colnext:
                continue
            else:
                x2 = colnext[(x, y)]
            if (x2, y2) in seen and count(
                quad, xmin, xmax, ymin, ymax, x, x2, y, y2, 0
            ) == 4:
                ret = max(ret, (y2 - y) * (x2 - x))
        return ret
