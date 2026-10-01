# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/


class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        positions = defaultdict(list)
        for i, c in enumerate(s):
            positions[c].append(i)
        chars = [c for c in positions]

        def interval(c):
            todo, rest = set(), set(chars)
            l, r = len(s), -1
            todo.add(c)
            rest.remove(c)
            while todo:
                u = todo.pop()
                l, r = min(l, positions[u][0]), max(r, positions[u][-1])
                for v in list(rest):
                    posv = positions[v]
                    if bisect_left(posv, l) != bisect_right(posv, r):
                        rest.remove(v)
                        todo.add(v)
            return l, r

        intervals = sorted(
            [list(interval(c)) for c in chars],
            key=lambda x: x[1]
        )
        ret, r = [], -1
        for a, b in intervals:
            if a > r:
                r = b
                ret.append(s[a:b + 1])
        return ret
