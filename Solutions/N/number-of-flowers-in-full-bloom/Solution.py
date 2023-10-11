# https://leetcode.com/problems/number-of-flowers-in-full-bloom/

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        points = []
        for start, end in flowers:
            points. extend([[start, -1], [end, 1]])
        for i, p in enumerate(people):
            points. append([p, 0, i])
        points = sorted(points)

        tot = 0
        for point in points:
            x, t, *_ = point
            if not t:
                people[point[2]] = -tot
            else:
                tot += t

        return people
