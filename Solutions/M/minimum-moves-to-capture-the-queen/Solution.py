# https://leetcode.com/problems/minimum-moves-to-capture-the-queen/

from queue import Queue


class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        bfsq = Queue()
        dist = {(a, b, c, d): 0}
        bfsq.put((a, b, c, d))
        dr = [[[0, 1], [0, -1], [1, 0], [-1, 0]], [[1, 1], [1, -1], [-1, -1], [-1, 1]]]
        while bfsq:
            a, b, c, d = bfsq.get()
            cur = dist[(a, b, c, d)]
            next = cur + 1
            for i in [0, 1]:
                for dx, dy in dr[i]:
                    pos = [[a, b], [c, d]]
                    while True:
                        pos[i][0] += dx
                        pos[i][1] += dy
                        postuple = (pos[0][0], pos[0][1], pos[1][0], pos[1][1])
                        if [e, f] in pos:
                            return next
                        elif pos[i][0] < 1 or pos[i][0] > 8 or pos[i][1] < 1 or pos[i][1] > 8 or pos[0] == pos[1]:
                            break
                        elif postuple not in dist:
                            dist[postuple] = next
                            bfsq.put(postuple)
        return -1
