# https://leetcode.com/problems/second-minimum-time-to-reach-destination/

import queue


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u] += [v]
            adj[v] += [u]

        dist1, dist2 = [[-1] * (n + 1) for _ in [0, 1]]

        def bfs(start, dist):
            dist[start] = 0
            bfsq = queue.Queue()
            bfsq.put(start)
            while not bfsq.empty():
                u = bfsq.get()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        bfsq.put(v)
        bfs(1, dist1)
        bfs(n, dist2)

        steps = dist2[1] + 2
        for u, v in edges:
            if dist2[1] in (dist1[u] + dist2[v], dist1[v] + dist2[u]):
                steps -= 1
                break
        t, switch = 0, 2 * change
        for i in range(steps):
            if t % switch >= change:
                t = (t // switch + 1) * switch
            t += time
        return t
