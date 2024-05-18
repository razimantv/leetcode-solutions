# https://leetcode.com/problems/maximum-points-inside-the-square/

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        seen = defaultdict(list)
        for (x, y), t in zip(points, s):
            seen[t].append(max(abs(x), abs(y)))

        lim = min(
            [sorted(v)[1] for v in seen.values() if len(v) > 1],
            default=10 ** 10
        )
        return sum(1 for x, y in points if max(abs(x), abs(y)) < lim)
