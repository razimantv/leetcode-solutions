# https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo:

    def __init__(self):
        self.intervals = [(0, 10 ** 9, 0)]

    def book(self, start: int, end: int) -> bool:
        end, next = end - 1, []
        for s, e, c in self.intervals:
            if s > end or e < start:
                next.append((s, e, c))
                continue
            if c == 2:
                return False
            if start <= s and e <= end:
                next.append((s, e, c+1))
            elif s <= start and end <= e:
                if s < start:
                    next.append((s, start - 1, c))
                next.append((start, end, c + 1))
                if end < e:
                    next.append((end + 1, e, c))
            elif s > start:
                next.append((s, end, c + 1))
                next.append((end + 1, e, c))
            else:
                next.append((s, start - 1, c))
                next.append((start, e, c + 1))
        self.intervals = next
        return True
