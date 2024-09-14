# https://leetcode.com/problems/length-of-the-longest-increasing-path/

class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        xk, yk = coordinates[k]
        good = sorted(
            [(x, y) for x, y in coordinates if (x - xk) * (y - yk) > 0],
            key=lambda x: (x[0], -x[1])
        )

        lis = []
        for _, x in good:
            pos = bisect_left(lis, x)
            if pos == len(lis):
                lis.append(x)
            else:
                lis[pos] = x
        return len(lis) + 1
