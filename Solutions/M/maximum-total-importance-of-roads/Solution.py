# https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = sorted(
            Counter((u for road in roads for u in road)). values(),
            reverse=True
        )
        return sum(x * y for x, y in zip(degrees, range(n, 0, -1)))
