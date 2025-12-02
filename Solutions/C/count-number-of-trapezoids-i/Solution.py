# https://leetcode.com/problems/count-number-of-trapezoids-i/

class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        pairs = [
            c * (c - 1) // 2 for c in Counter((y for x, y in points)).values()
        ]
        tot = sum(pairs)
        return (sum((p * (tot - p) for p in pairs)) // 2) % (10 ** 9 + 7)
