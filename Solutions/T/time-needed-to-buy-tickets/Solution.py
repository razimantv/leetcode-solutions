# https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(
            min(x, tickets[k] - (1 if i > k else 0))
            for i, x in enumerate(tickets)
        )
