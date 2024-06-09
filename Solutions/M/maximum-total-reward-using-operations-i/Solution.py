# https://leetcode.com/problems/maximum-total-reward-using-operations-i/

from sortedcontainers import SortedList


class Solution:
    def maxTotalReward(self, rewards: List[int]) -> int:
        sl, ret = SortedList([(0, 0)]), 0
        rewards = sorted(list(set(rewards)))

        def add(l, r):
            idx = sl. bisect_left((l, l))
            if idx and sl[idx - 1][1] >= l - 1:
                pl, pr = sl.pop(idx - 1)
                l, r = pl, max(r, pr)
            while True:
                idx = sl. bisect_left((l, l))
                if idx < len(sl) and sl[idx][0] <= r + 1:
                    pl, pr = sl.pop(idx)
                    r = max(r, pr)
                else:
                    break
            sl.add((l, r))

        for x in rewards:
            todo = []
            for l, r in sl:
                if l >= x:
                    break
                r = min(r, x - 1)
                ret = max(ret, r + x)
                if l + x < rewards[-1]:
                    todo.append([l + x, min(r + x, rewards[-1])])
            for l, r in todo:
                add(l, r)
        return ret
