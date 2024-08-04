# https://leetcode.com/problems/alternating-groups-iii/

from sortedcontainers import SortedList


class Solution:
    def numberOfAlternatingGroups(
        self, colors: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(colors)
        colors += colors

        sl, base = SortedList(), 1
        while base <= n:
            base <<= 1
        seg = [[0, 0] for _ in range(2 * base)]

        def update(x, delta):
            node = x + base
            while node:
                seg[node][0] += delta
                seg[node][1] += delta * x
                node >>= 1

        def insert(l, r):
            l, r = l % n, r % n
            if r < l:
                r += n
            sl.add((l, r))
            update(r - l + 1, 1)

        def get_component(pos):
            pos %= n
            if pos < sl[0][0]:
                pos += n
            index = sl.bisect_right((pos, 3 * n)) - 1
            l, r = sl.pop(index)
            update(r - l + 1, -1)
            return l, r, pos

        l = 0
        for r in range(1, 2 * n):
            if colors[r] == colors[r-1]:
                if l:
                    insert(l, r-1)
                if r > n:
                    break
                l = r
        else:
            insert(0, n - 1)

        ret = []
        for query in queries:
            if query[0] == 1:
                size = query[1]
                if len(sl) == 1:
                    ret.append(n - size + 1 if n & 1 else n)
                    continue
                node = size + base
                cnt, tot = seg[node]
                while node > 1:
                    if not (node & 1):
                        cnt += seg[node ^ 1][0]
                        tot += seg[node ^ 1][1]
                    node >>= 1
                ret.append(tot - (size - 1) * cnt)
            else:
                index, color = query[1:]
                if colors[index] == color:
                    continue
                colors[index] = colors[index + n] = color
                l, r, index = get_component(index)
                if len(sl) == 0:
                    if not (n & 1):
                        insert(index, index)
                        insert(index + 1, index + n - 1)
                    else:
                        if index == l:
                            insert(index + 1, index)
                        elif index == r:
                            insert(index, index + n - 1)
                        else:
                            insert(l, index + n - 1)
                            insert(index, index)
                            insert(index + 1, r)
                elif l < index < r:
                    insert(l, index + n - 1)
                    insert(index, index)
                    insert(index + 1, r)
                elif l == r:
                    if len(sl) == 1:
                        get_component(l + n - 1)
                        insert(0, n - 1)
                    else:
                        ll = get_component(l + n - 1)[0]
                        rr = get_component(r + 1)[1]
                        insert(ll, rr)
                elif index == l:
                    ll = get_component(l + n - 1)[0]
                    insert(ll, l)
                    insert(l + 1, r)
                elif index == r:
                    rr = get_component(r + 1)[1]
                    insert(l, r + n - 1)
                    insert(r, rr)

        return ret
