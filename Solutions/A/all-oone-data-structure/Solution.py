# https://leetcode.com/problems/all-oone-data-structure/

class AllOne:

    def __init__(self):
        self.count, self.inv = {}, {}

    def inc(self, key: str) -> None:
        count, inv = self.count, self.inv
        if key not in count:
            count[key] = 1
        else:
            inv[count[key]].remove(key)
            if not inv[count[key]]:
                del inv[count[key]]
            count[key] += 1
        if count[key] not in inv:
            inv[count[key]] = set()
        inv[count[key]].add(key)

    def dec(self, key: str) -> None:
        count, inv = self.count, self.inv
        inv[count[key]].remove(key)
        if not inv[count[key]]:
            del inv[count[key]]
        count[key] -= 1
        if not count[key]:
            del count[key]
        else:
            if count[key] not in inv:
                inv[count[key]] = set()
            inv[count[key]].add(key)

    def getMaxKey(self) -> str:
        inv = self.inv
        if not inv:
            return ""
        return next(iter(inv[max(inv)]))

    def getMinKey(self) -> str:
        inv = self.inv
        if not inv:
            return ""
        return next(iter(inv[min(inv)]))
