# https://leetcode.com/problems/walking-robot-simulation-ii/

dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]
names = ["East", "North", "West", "South"]


class Robot:

    def __init__(self, width: int, height: int):
        self.w, self.h, self.x, self.y, self.dir = width, height, 0, 0, 0

    def step(self, num: int) -> None:
        while num:
            nextx, nexty = self.x + dr[self.dir][0], self.y + dr[self.dir][1]
            if 0 <= nextx < self.w and 0 <= nexty < self.h:
                self.x, self.y, num = nextx, nexty, num - 1
            else:
                break
        num %= 2 * (self.w + self.h) - 4
        while num:
            nextx, nexty = self.x + dr[self.dir][0], self.y + dr[self.dir][1]
            if 0 <= nextx < self.w and 0 <= nexty < self.h:
                self.x, self.y, num = nextx, nexty, num - 1
            else:
                self.dir = (self.dir + 1) & 3

    def getPos(self) -> list[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return names[self.dir]
