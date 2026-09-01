# https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

import queue


class Solution:
    def minMoves(self, room: list[str], energy: int) -> int:
        m, n = len(room), len(room[0])
        litter = {}
        for i, row in enumerate(room):
            for j, c in enumerate(row):
                if c == 'S':
                    si, sj = i, j
                elif c == 'L':
                    litter[(i, j)] = 1 << len(litter)
        L = len(litter)
        if not L:
            return 0
        bfsq = queue.Queue()
        bfsq.put((si, sj, (1 << L) - 1, energy))
        dist = [
            [[[-1] * (energy + 1) for _ in range(1 << L)] for _ in range(n)]
            for _ in range(m)
        ]
        dist[si][sj][(1 << L) - 1][energy] = 0
        beste = [[[0] * (1 << L) for _ in range(n)] for _ in range(m)]
        while not bfsq. empty():
            i, j, mask, e = bfsq.get()
            if e <= beste[i][j][mask]:
                continue
            beste[i][j][mask] = e
            d = dist[i][j][mask][e]
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ii, jj = i + di, j + dj
                if not (0 <= ii < m and 0 <= jj < n and room[ii][jj] != 'X'):
                    continue
                newdist = d + 1
                newmask = mask & ~litter. get((ii, jj), 0)
                if not newmask:
                    return newdist
                newe = energy if room[ii][jj] == 'R' else e - 1
                if dist[ii][jj][newmask][newe] == -1:
                    dist[ii][jj][newmask][newe] = newdist
                    bfsq.put((ii, jj, newmask, newe))
        return -1
