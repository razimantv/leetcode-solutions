# https://leetcode.com/problems/smallest-substring-with-identical-characters-ii

class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        ends = [-1] + [
            i for i, (x, y) in enumerate(pairwise(s)) if x != y
        ] + [n - 1]
        groups = [y - x for x, y in pairwise(ends)]

        def work(x):
            if x == 1:
                cnt = sum([
                    1 for i, c in enumerate(s)
                    if c == ('0' if i & 1 else '1')
                ])
                return min(cnt, n - cnt) <= numOps
            return sum(g // (x + 1) for g in groups) <= numOps

        start, end = 0, n
        while end - start > 1:
            mid = (start + end) // 2
            if work(mid):
                end = mid
            else:
                start = mid
        return end
