# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        cost1 = min(cost1, costBoth)
        cost2 = min(cost2, costBoth)
        costBoth = min(cost1 + cost2, costBoth)
        ret = (a := min(need1, need2)) * costBoth
        return ret + (need1 - a) * cost1 + (need2 - a) * cost2
