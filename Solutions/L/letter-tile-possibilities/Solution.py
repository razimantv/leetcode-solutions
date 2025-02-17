# https://leetcode.com/problems/letter-tile-possibilities

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        @cache
        def work(mask):
            if not mask:
                return set([''])
            ret = set()
            for i in range(len(tiles)):
                if not (mask & (1 << i)):
                    continue
                cur = work(mask ^ (1 << i))
                for s in cur:
                    ret.add(s)
                    ret.add(s + tiles[i])

            return ret

        return len(work((1 << len(tiles)) - 1)) - 1
