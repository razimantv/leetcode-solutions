# https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.ar = [0] * k
        self.head, self.tail, self.n, self.k = 1 % k, 0, 0, k

    def insertFront(self, value: int) -> bool:
        if self.n == self.k:
            return False
        self.n += 1
        self.head = (self.head + self.k - 1) % self.k
        self.ar[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.n == self.k:
            return False
        self.n += 1
        self.tail = (self.tail + 1) % self.k
        self.ar[self.tail] = value
        return True

    def deleteFront(self) -> bool:
        if not self.n:
            return False
        self.n -= 1
        self.head = (self.head + 1) % self.k
        return True

    def deleteLast(self) -> bool:
        if not self.n:
            return False
        self.n -= 1
        self.tail = (self.tail + self.k - 1) % self.k
        return True

    def getFront(self) -> int:
        return self.ar[self.head] if self.n else -1

    def getRear(self) -> int:
        return self.ar[self.tail] if self.n else -1

    def isEmpty(self) -> bool:
        return not self.n

    def isFull(self) -> bool:
        return self.n == self.k
