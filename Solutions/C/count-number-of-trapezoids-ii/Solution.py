# https://leetcode.com/problems/count-number-of-trapezoids-ii/

def slope(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    g = gcd(dx, dy)
    dx, dy = dx // g, dy // g
    if (dx, dy) <= (0, 0):
        dx, dy = -dx, -dy
    return (dx, dy)


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        mid_to_m, m_to_c = defaultdict(list), defaultdict(list)

        for i, (x1, y1) in enumerate(points):
            for j in range(i):
                x2, y2 = points[j]
                m = slope(x1, y1, x2, y2)
                c = y1 * m[0] - x1 * m[1]
                mid = (x1 + x2, y1 + y2)
                mid_to_m[mid].append(m)
                m_to_c[m].append(c)

        ret = 0
        for intercepts in m_to_c.values():
            prev = 0
            for x in Counter(intercepts).values():
                ret += x * prev
                prev += x

        for slopes in mid_to_m.values():
            prev = 0
            for x in Counter(slopes).values():
                ret -= x * prev
                prev += x

        return ret
