# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        n = len(inventory)

        def cnt(x):
            return sum(max(0, a - x + 1) for a in inventory)

        start, end = 0, max(inventory) + 1
        while end - start > 1:
            mid = (start + end) // 2
            if cnt(mid) >= orders:
                start = mid
            else:
                end = mid

        ret = 0
        for item in inventory:
            times = max(0, item - start)
            ret += times * (item + start + 1) // 2
            orders -= times
        ret += orders * start
        return ret % (10 ** 9 + 7)
