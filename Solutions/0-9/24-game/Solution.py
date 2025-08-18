# https://leetcode.com/problems/24-game/

@cache
def submasks(mask):
    return [x for x in range(1, mask) if (x & mask) == x]


inv = {1: 0, 2: 1, 4: 2, 8: 3}


class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        @cache
        def work(mask):
            if not mask & (mask - 1):
                return set([cards[inv[mask]]])
            ret = set()
            for sub in submasks(mask):
                for x in work(sub):
                    for y in work(mask ^ sub):
                        for op in [operator.add, operator.mul, operator. sub]:
                            ret.add(op(x, y))
                        if y:
                            ret.add(x / y)
            return ret

        return min(abs(24 - x) for x in work(15)) < 1e-6
