# https://leetcode.com/problems/implement-router/

import queue


class Router:

    def __init__(self, limit: int):
        self.data = queue.Queue()
        self.n = limit
        self.set = set()
        self.times = defaultdict(SortedList)

    def addPacket(self, s: int, d: int, t: int) -> bool:
        packet = (s, d, t)
        if packet in self.set:
            return False
        if self.data.qsize() == self.n:
            self.forwardPacket()
        self.data.put(packet)
        self.set.add(packet)
        self.times[d].add(t)
        return True

    def forwardPacket(self) -> list[int]:
        if self.data.empty():
            return []
        packet = self.data.get()
        self.set.remove(packet)
        self.times[packet[1]].pop(self.times[packet[1]].bisect_left(packet[2]))
        return list(packet)

    def getCount(self, destination: int, start: int, end: int) -> int:
        return (
            self.times[destination].bisect_right(end) -
            self.times[destination].bisect_left(start)
        )
