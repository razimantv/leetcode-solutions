# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

class Solution:
    def smallestChair(self, times: List[List[int]], target: int) -> int:
        n = len(times)
        free = list(range(n))
        times = sorted([
            (t[j], -j, i)
            for i, t in enumerate(times)
            for j in (0, 1)
        ])

        chairs = [0] * n
        for t, ad, i in times:
            if ad == -1:
                heapq.heappush(free, chairs[i])
            else:
                chairs[i] = heapq.heappop(free)
        return chairs[target]
