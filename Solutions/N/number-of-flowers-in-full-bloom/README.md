# Number of flowers in full bloom

[Problem link](https://leetcode.com/problems/number-of-flowers-in-full-bloom/)

## Solutions


### Solution.py
```py
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
```
## Tags

* [Intervals](/Collections/intervals.md#intervals) > [Endpoint sorting](/Collections/intervals.md#endpoint-sorting)
* [Intervals](/Collections/intervals.md#intervals) > [Overlap](/Collections/intervals.md#overlap)
* [Sorting](/Collections/sorting.md#sorting) > [Queries and updates together](/Collections/sorting.md#queries-and-updates-together)
